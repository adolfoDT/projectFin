from flask import Blueprint, request, redirect, current_app
import hashlib

main = Blueprint('main', __name__)

@main.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
    current_app.redis.set(short_url, original_url)  # Usa current_app para acceder a la conexión Redis
    return f'Short URL: http://localhost:5001/{short_url}'

@main.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = current_app.redis.get(short_url)  # Usa current_app para acceder a la conexión Redis
    if original_url:
        current_app.redis.incr(f'count:{short_url}')
        return redirect(original_url.decode())
    else:
        return 'URL not found', 404

@main.route('/stats/<short_url>')
def link_stats(short_url):
    access_count = current_app.redis.get(f'count:{short_url}')
    if access_count:
        return f'The short link {short_url} has been accessed {access_count.decode()} times.'
    else:
        return 'No access data found for this short link.', 404