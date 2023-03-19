## MySQL Queries

#### a. How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger?
Solution
* Query to find tigers from taxonomy
```sql
SELECT ncbi_id, species 
FROM taxonomy 
WHERE species LIKE '%Panthera tigris%';
```
* Query to find number of tigers
```sql
SELECT COUNT(*) AS no_of_types 
FROM taxonomy 
WHERE species LIKE '%Panthera tigris%'
```
* Query to find ncbi_id of the Sumatran Tiger
```sql
SELECT ncbi_id,species 
FROM taxonomy 
WHERE species LIKE '%Sumatran tiger%'
```
#### b. Find all the columns that can be used to connect the tables in the given database
Solution
```txt
ncbi_id from taxonomy
ncbi_id from rfamseq
rfamseq_acc from rfamseq
rfamseq_acc from full_region
rfam_acc from family
rfam_acc from full_region
clan_acc from clan_membership
clan_acc from clan_membership
```
