from .gourmet_model import Ingredients,Categories,Convtable,Keylookup,PluginInfo,Shopcats,Unitdict,Crossunitdict,Shopcatsorder,Density,Info,Pantry,Recipe

class ApiRouter(object):
    def _is_gourmet_model(self, model):
        if model == Ingredients or model == Categories or model == Convtable or model == Keylookup or model == PluginInfo or model == Shopcats or model == Unitdict or model == Crossunitdict or model == Shopcatsorder or model == Density or model== Info or model == Pantry or model == Recipe:
            return True
        return False

    def db_for_read(self, model, **hints):
        if self._is_gourmet_model(model):
            return 'recipes_db'
        return None

    def db_for_write(self, model, **hints):
        if self._is_gourmet_model(model):
            return 'recipes_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        return True