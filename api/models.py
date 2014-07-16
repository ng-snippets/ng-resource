from google.appengine.ext import ndb

class Contact(ndb.Model):

    name = ndb.StringProperty(required = True)

    email = ndb.StringProperty(required = True)

    phone = ndb.StringProperty(required = True)

    #TODO user photo needs to be added later

    def to_dict(self):
        results =super(Contact,self).to_dict()
        results['id'] = self.key.id() ^ 0xBADAD
        return results

