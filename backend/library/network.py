import logging
from typing import List, Dict
from collections import defaultdict

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def process_hashtags(all_statuses: List[List[Dict]], searched_hashtag: str) -> Dict:
    co_occurrence = defaultdict(set)  # Using a dictionary to hold co-occurrence sets
    nodes = {}  # Initialize nodes for hashtags
    edges = []  # Initialize edges for co-occurrence relationships

    unique_hashtags = set()  # Use a set to store unique hashtags

    # Loop through the statuses
    for statuses in all_statuses:
        for status in statuses:
            # Check if the status has tags
            if 'tags' in status and status['tags']:
                # Extract hashtags from the status
                hashtags = [tag['name'] for tag in status['tags']]

                # Remove the searched hashtag to avoid hair loops
                hashtags = [tag for tag in hashtags if tag != searched_hashtag]

                unique_hashtags.update(hashtags)  # Add hashtags to the set

                # Add co-occurrence relationships between hashtags
                for i in range(len(hashtags)):
                    for j in range(i + 1, len(hashtags)):
                        co_occurrence[hashtags[i]].add(hashtags[j])
                        co_occurrence[hashtags[j]].add(hashtags[i])

    # Create nodes with hashtag names as labels
    for index, hashtag in enumerate(co_occurrence.keys()):
        nodes[hashtag] = {
            "label": f'#{hashtag}'
        }

    # Create edges based on co-occurring hashtags
    for hashtag, co_tags in co_occurrence.items():
        for co_tag in co_tags:
            edges.append({
                "source": hashtag,
                "target": co_tag
            })

    logger.info(f"Total unique hashtags processed: {len(unique_hashtags)}")
    logger.info(f"Total co-occurrence pairs: {len(co_occurrence)}")
    logger.info(f"Nodes count: {len(nodes)}")
    logger.info(f"Edges count: {len(edges)}")

    return {"nodes": nodes, "edges": edges}


