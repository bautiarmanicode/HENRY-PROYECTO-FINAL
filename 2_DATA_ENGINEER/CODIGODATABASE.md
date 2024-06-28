
CREATE DATABASE yelp_google;

USE yelp_google;

CREATE TABLE Dim_User (
    user_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    yelping_since DATE,
    review_count INT,
    useful INT,
    funny INT,
    cool INT,
    elite VARCHAR(255),
    average_stars FLOAT
);

CREATE TABLE Dim_Business (
    business_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postal_code VARCHAR(20),
    latitude FLOAT,
    longitude FLOAT,
    stars FLOAT,
    review_count INT,
    is_open BOOLEAN,
    categories TEXT
);

CREATE TABLE Fact_Review (
    review_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255),
    business_id VARCHAR(255),
    rating INT,
    date DATE,
    text TEXT,
    pics TEXT,
    resp TEXT,
    FOREIGN KEY (user_id) REFERENCES Dim_User(user_id),
    FOREIGN KEY (business_id) REFERENCES Dim_Business(business_id)
);
