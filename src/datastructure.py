class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []
        # Miembros iniciales
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })
        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })
        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Si no viene id, lo generamos
        if 'id' not in member or member['id'] is None:
            member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        for i, m in enumerate(self._members):
            if m['id'] == id:
                del self._members[i]
                return True
        return False

    def get_member(self, id):
        for m in self._members:
            if m['id'] == id:
                return m
        return None

    def get_all_members(self):
        return self._members