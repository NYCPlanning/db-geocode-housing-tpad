<h1>db-geocode-housing-tpad</h1>
<h3>GRU Housing Geocode TPAD QAQC Project</h3>
<p>This project reads the housing database for records where the certificate of occupancy
earliest effective date has a value. It then calls Geosupport using function 1B to identify
records in TPAD.</p>

<h4>Instructions:</h4>
<ol>
<li>Download records from the housing database from the Capital Planning website, in CSV format.</li>
<li>'sh 01_initialize.sh' to spin up a postgreSQL container</li>
<li>'sh 02_geocoding.sh' to select and geocode BINs (Geosupport function BN)</li>
<li>'sh 03_export.sh' to output the table of geocoded BINs</li>
<li>'sh 04_cleanup.sh' to clean up the postgreSQL container</li>
</ol>
