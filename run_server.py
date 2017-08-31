#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~

from threading import Thread
import os
import subprocess

try:
    from config import config as env_config, env

    CONFIG = env_config.get(env, 'default')()
except ImportError:
    CONFIG = type('_', (), {'__getattr__': None})()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

apps_dir = os.path.join(BASE_DIR, 'apps')


def start_django():
    http_host = CONFIG.HTTP_BIND_HOST or '127.0.0.1'
    http_port = CONFIG.HTTP_LISTEN_PORT or '8080'
    os.chdir(apps_dir)
    print('start django')
    subprocess.call('python ./manage.py runserver %s:%s' % (http_host, http_port), shell=True)


<<<<<<< HEAD
def start_celery():
    os.chdir(apps_dir)
    os.environ.setdefault('C_FORCE_ROOT', '1')
    os.environ.setdefault('PYTHONOPTIMIZE', '1')
    print('start celery')
    subprocess.call('celery -A common worker -B -s /tmp/celerybeat-schedule -l debug', shell=True)
=======
    def forward_outbound(self):
        self.log_file_f, self.log_time_f, self.log = self.term.get_log()
        self.id = self.log.id
        self.termlog.setid(self.id)
        try:
            data = ''
            pre_timestamp = time.time()
            while True:
                r, w, e = select.select([self.channel], [], [])
                if self.channel in r:
                    recv = self.channel.recv(1024)
                    if not len(recv):
                        return
                    data += recv
                    self.term.vim_data += recv
                    try:
                        self.write_message(data.decode('utf-8', 'replace'))
                        self.termlog.write(data)
                        self.termlog.recoder = False
                        now_timestamp = time.time()
                        self.log_time_f.write('%s %s\n' % (round(now_timestamp - pre_timestamp, 4), len(data)))
                        self.log_file_f.write(data)
                        pre_timestamp = now_timestamp
                        self.log_file_f.flush()
                        self.log_time_f.flush()
                        if self.term.input_mode:
                            self.term.data += data
                        data = ''
                    except UnicodeDecodeError:
                        pass
        except IndexError:
            pass
>>>>>>> a114e173e07837831c78669bbd1546e430e4b7fc


def main():
    t1 = Thread(target=start_django, args=())
    t2 = Thread(target=start_celery, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()


<<<<<<< HEAD
=======
def main():
    from django.core.wsgi import get_wsgi_application
    import tornado.wsgi
    wsgi_app = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    setting = {
        'cookie_secret': 'DFksdfsasdfkasdfFKwlwfsdfsa1204mx',
        'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'debug': False,
    }
    tornado_app = tornado.web.Application(
        [
            (r'/ws/monitor', MonitorHandler),
            (r'/ws/terminal', WebTerminalHandler),
            (r'/ws/kill', WebTerminalKillHandler),
            (r'/ws/exec', ExecHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler,
             dict(path=os.path.join(os.path.dirname(__file__), "static"))),
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ], **setting)
>>>>>>> a114e173e07837831c78669bbd1546e430e4b7fc




