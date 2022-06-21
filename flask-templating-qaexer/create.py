from app import db, Countries, Cities, Borough, Owner

db.drop_all()
db.create_all() # Creates all table classes defined

uk = Countries(name = 'United Kingdom') #Add example to countries table
db.session.add(uk)
db.session.commit()

# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
ldn = Cities(name='London', country = uk)
mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()

b1 = Borough(name="Newham", borough= uk)
b2 = Borough(name="Barking", borough= uk)
db.session.add(b1)
db.session.add(b2)
db.session.commit()

#print({uk.cities.name.all()})
#print("ok")

print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
print(f"London's country is: {ldn.country.name}")
print(f"Manchester's country is: {ldn.country.name}")
print(f"Newham's country is: {b1.borough.name}")