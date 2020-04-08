class DbHelper(object):
    def get_or_create(self, session, model, **kwargs):
        """
        Create an object or returns the object if exists
        credit to Kevin @ StackOverflow
        from: http://stackoverflow.com/questions/2546207/does-sqlalchemy-have-an-equivalent-of-djangos-get-or-create
        """
        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = model(**kwargs)
            session.add(instance)
            session.commit()
            return instance
