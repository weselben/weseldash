-- PostgreSQL Extensions for Personal Dashboard
-- This script sets up useful extensions for the dashboard

-- Enable UUID extension for generating UUIDs
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enable pgcrypto for password hashing and encryption
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Enable full-text search capabilities
CREATE EXTENSION IF NOT EXISTS "unaccent";

-- Enable vector similarity search (if pg_vector is available)
-- CREATE EXTENSION IF NOT EXISTS "vector";

-- Create indexes for better performance
-- Additional indexes will be created by SQLAlchemy/Alembic

-- Set timezone
SET timezone = 'UTC';