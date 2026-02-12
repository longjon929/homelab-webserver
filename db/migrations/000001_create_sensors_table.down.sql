-- 1. Drop the transaction table (and its indexes) first
DROP TABLE IF EXISTS readings;

-- 2. Drop the reference tables (order between these two doesn't matter)
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS sensors;