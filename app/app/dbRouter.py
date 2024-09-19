class DbRouter:
    def db_for_read(self, model, **hints) -> str:
        if hasattr(model, '_db'):
            return model._db
        return 'default'

    def db_for_write(self, model, **hints) -> str:
        if hasattr(model, '_db'):
            return model._db
        return 'default'

    def allow_relation(self, obj1, obj2, **hints) -> bool:
        return True
        # return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        #return True
        if app_label == 'app_manager':
            return db == 'menu'
        return None