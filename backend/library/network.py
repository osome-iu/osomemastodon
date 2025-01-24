import logging
from typing import List, Dict
from collections import defaultdict
from urllib.parse import urlparse

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def parse_domain_and_username(user_identifier):
    """
    Extract the domain and username from a URL and
    Return a tuple (domain, username).

    Parameters:
    user_identifier (str): The URL of the user.
    type (str): The type of return value ('author_file' for string, otherwise tuple).

    Returns:
    tuple: domain, username
    """
    try:
        parsed_url = urlparse(user_identifier)
        domain = parsed_url.netloc
        # Split the path and filter out empty parts
        path_parts = [part for part in parsed_url.path.split('/') if part]
        # Get the last non-empty part of the path as the username
        username = path_parts[-1].strip("@") if path_parts else ""
        return domain, username
    except Exception as e:
        logger.error(f"Error parsing URL: {e}")
        return None


def process_hashtags(all_statuses: List[List[Dict]], searched_hashtag: str) -> Dict:
    co_occurrence = defaultdict(set)  # Dictionary to hold co-occurrence sets
    nodes = {}  # Dictionary for nodes with hashtag labels and multiple domains
    edges = []  # List for edges with co-occurrence relationships
    unique_hashtags = set()  # Set to track unique hashtags
    edge_set = set()  # Set to track unique edges

    for statuses in all_statuses:
        for status in statuses:
            # Check if the status has tags
            if 'tags' in status and status['tags']:
                # Extract hashtags from the status
                hashtags = [tag['name'] for tag in status['tags']]

                # Remove the searched hashtag to avoid hair loops
                hashtags = [tag for tag in hashtags if tag != searched_hashtag]

                # Add hashtags to the unique set
                unique_hashtags.update(hashtags)

                # Get domain and username
                domain, username = parse_domain_and_username(status.get('url', None))

                # Track co-occurrence relationships
                for i in range(len(hashtags)):
                    for j in range(i + 1, len(hashtags)):
                        hashtag1 = hashtags[i]
                        hashtag2 = hashtags[j]

                        # Add co-occurrence relationships
                        co_occurrence[hashtag1].add(hashtag2)
                        co_occurrence[hashtag2].add(hashtag1)

                        # Ensure the node for each hashtag exists
                        if hashtag1 not in nodes:
                            nodes[hashtag1] = {
                                "label": hashtag1,
                                "domains": []  # Initialize an empty list for domains
                            }
                        if hashtag2 not in nodes:
                            nodes[hashtag2] = {
                                "label": hashtag2,
                                "domains": []  # Initialize an empty list for domains
                            }

                        # Add the domain to the node if it's not already in the list
                        if domain and domain not in nodes[hashtag1]["domains"]:
                            nodes[hashtag1]["domains"].append(domain)
                        if domain and domain not in nodes[hashtag2]["domains"]:
                            nodes[hashtag2]["domains"].append(domain)

                        # Create a unique edge identifier
                        edge_key = frozenset([hashtag1, hashtag2])

                        if edge_key not in edge_set:
                            edge_set.add(edge_key)
                            edges.append({
                                "source": hashtag1,
                                "target": hashtag2,
                                "type": "co-occurrence",
                                "posts": [{
                                    "uri": status.get('url', None),
                                    "indexedAt": status.get('created_at', None),
                                    "tags": hashtags,
                                    "domain": domain, 
                                    "type": "co-occurrence"
                                }]
                            })

    # Log the results
    logger.info(f"For the searched hashtag '{searched_hashtag}', total unique hashtags: {len(unique_hashtags)}")
    logger.info(f"Total co-occurrence pairs: {sum(len(v) for v in co_occurrence.values()) // 2}")
    logger.info(f"Number of nodes: {len(nodes)}")
    logger.info(f"Number of edges: {len(edges)}")

    return {"nodes": nodes, "edges": edges}


