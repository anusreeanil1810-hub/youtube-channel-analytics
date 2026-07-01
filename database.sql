CREATE TABLE channels (
    id INTEGER PRIMARY KEY,
    channel_name VARCHAR(100),
    subscribers BIGINT,
    views BIGINT,
    videos INT,
    country VARCHAR(50),
    description TEXT
);