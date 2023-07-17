-- create table user
create table users(
	id VARCHAR(255) PRIMARY KEY,
	instance VARCHAR(255) NOT NULL,
	username VARCHAR(255) NOT NULL,
	acct VARCHAR(255) NOT NULL,
	display_name VARCHAR(20),
	locked BOOLEAN NOT NULL,
	bot BOOLEAN NOT NULL,
	created_at DATE,
	followers_count INTEGER,
	following_count INTEGER,
	statuses_count INTEGER,
	last_status_at DATE
);

-- create table posts
create table posts(
	id VARCHAR(255) PRIMARY KEY,
	instance VARCHAR(255) NOT NULL,
	user_id VARCHAR(255) NOT NULL,
	user_name VARCHAR(255) NOT NULL,
	is_bot BOOLEAN NOT NULL,
	post VARCHAR(255) NOT NULL,
	url VARCHAR(255) NOT NULL
)