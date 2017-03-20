


unload  ('select * from venue order by venueid')
manifest 
delimiter '|';


copy venue 
manifest 
delimiter '|';
