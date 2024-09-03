from django.shortcuts import render
from .ml_models import predict_phishing  # Import your function for phishing detection

# For simplicity, let's assume you store recent URLs in a session
RECENT_URLS_LIMIT = 10

def update_recent_urls(request, url):
    # Get recent URLs from session
    recent_urls = request.session.get('recent_urls', [])

    # Update recent URLs
    if url not in recent_urls:
        recent_urls.insert(0, url)  # Add to the beginning of the list
        if len(recent_urls) > RECENT_URLS_LIMIT:
            recent_urls.pop()  # Remove the oldest URL if limit exceeded
        request.session['recent_urls'] = recent_urls

def home(request):
    is_phishing = None
    url = None
    recent_urls = request.session.get('recent_urls', [])

    if request.method == 'POST':
        url = request.POST.get('url', '')
        if url:
            is_phishing = predict_phishing(url)
            update_recent_urls(request, url)

    return render(request, 'detection/home.html', {
        'url': url,
        'is_phishing': is_phishing,
        'recent_urls': recent_urls,
    })

def url_detection(request):
    is_phishing = None
    url = None
    recent_urls = request.session.get('recent_urls', [])

    if request.method == 'POST':
        url = request.POST.get('url', '')
        if url:
            is_phishing = predict_phishing(url)
            update_recent_urls(request, url)

    return render(request, 'detection/url_detection.html', {
        'url': url,
        'is_phishing': is_phishing,
        'recent_urls': recent_urls,
    })
