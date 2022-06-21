
from app1 import db, Owners, Car

db.drop_all()
db.create_all()

# testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
# db.session.add(testuser)
# db.session.commit()

person1 = Owners(first_name="Dave", last_name="Smith")
db.session.add(person1)
db.session.commit()

car1 = Car(reg="WQA1 3TF", owner_id=person1)
db.session.add(car1)
db.session.commit()

car2 = Car(reg="WQB2 3ED", owner_id=person1)
db.session.add(car2)
db.session.commit()


print(person1.cars)

print(car1.ownerbr.last_name + ',  '+ car1.ownerbr.id)