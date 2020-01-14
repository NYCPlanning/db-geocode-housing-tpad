DROP TABLE IF EXISTS housing_geocode_tpad_errors;
SELECT geo_bbl, geo_bin, geo_tpad_new_bin, geo_tpad_new_bin_status,
geo_tpad_dm_bin_status, geo_tpad_conflict_flag, geo_tpad_bin_status,
geo_return_code, geo_return_code_2, geo_message, geo_message_2, geo_reason_code
INTO housing_geocode_tpad_errors
FROM housing_geocode
WHERE geo_return_code NOT IN ('00', '01', '22', '23');
