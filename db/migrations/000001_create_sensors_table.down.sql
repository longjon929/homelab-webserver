-- 1. Drop the transaction table (and its indexes) first
DROP TABLE IF EXISTS environment_data;
DROP INDEX IF EXISTS idx_environment_data_sensor_time;
DROP INDEX IF EXISTS idx_environment_data_location_time

DROP TABLE IF EXISTS soil_data;
DROP INDEX IF EXISTS idx_soil_sensor_time;
DROP INDEX IF EXISTS idx_soil_location_time;


-- 2. Drop the reference tables (order between these two doesn't matter)
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS sensors;