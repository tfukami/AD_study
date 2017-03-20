


unload  ('select * from venue order by venueid')
to 's3://mybucket/tickit/venue/reload_' 
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole' 
manifest 
delimiter '|';


copy venue 
from 's3://mybucket/tickit/venue/reload_manifest' 
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
manifest 
delimiter '|';
