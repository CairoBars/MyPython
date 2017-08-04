#Author:Cairo Li
class App(object):

    def add_url_rule(self,rule,endpoint=None,view_func=None,**options):
        methods=options.pop('methods',None)
        if methods is None:
            print("111")
            print(view_func)
            methods=getattr(view_func,'methods',None) or ('GET')
            print(methods)




    def route(self, rule, **options):
        """A decorator that is used to register a view function for a
        given URL rule.  This does the same thing as :meth:`add_url_rule`
        but is intended for decorator usage::

            @app.route('/')
            def index():
                return 'Hello World'

        For more information refer to :ref:`url-route-registrations`.

        :param rule: the URL rule as string
        :param endpoint: the endpoint for the registered URL rule.  Flask
                         itself assumes the name of the view function as
                         endpoint
        :param options: the options to be forwarded to the underlying
                        :class:`~werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options.  methods
                        is a list of methods this rule should be limited
                        to (``GET``, ``POST`` etc.).  By default a rule
                        just listens for ``GET`` (and implicitly ``HEAD``).
                        Starting with Flask 0.6, ``OPTIONS`` is implicitly
                        added and handled by the standard request handling.
        """
        def decorator(f):
            print("The f is:",f)
            f.methods="VVV"
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator


myapp=App()

@myapp.route("/")
def hello():
    setattr(hello,'kk','value')
    methods={'GET','POST'}
    return "hello"


setattr(hello,'kk','value')
print(hasattr(hello,'kk'))
print(hasattr(hello,'methods'))


s1="DDDD"
s2="DDDD"
print(id(s1))
print(id(s2))

print("s1 and s2:",s1==s2)


hello()