from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from scripts.models import Script

def pygmentIt(code):
    try:
        from pygments import highlight
        from pygments.lexers import guess_lexer
        from pygments.formatters import HtmlFormatter
        lexer = guess_lexer(code)
        return highlight(unicode(code), lexer, HtmlFormatter())
    except:
        return code

def index(request):
    latest_script_list = Script.objects.order_by('-publication_date')[:10]
    context = {'latest_script_list' : latest_script_list, }
    return render(request, 'scripts/index.html', context)

def detail(request, script_id):
    script = get_object_or_404(Script, pk=script_id)
    context = {'script' : script,}
    return render(request, 'scripts/view.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
