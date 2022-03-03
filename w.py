import json
import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/member')
def member():
    with open('templates/member.json', 'r', encoding='utf-8') as m:
        f = m.read()
        data = json.loads(f)
    a = random.choice(data['actors'])
    return render_template('index.html', name_actors=a['name'], foto=a['data']['foto'],
                           specialization='; '.join(sorted(a["data"]['specialization'])))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.12')
