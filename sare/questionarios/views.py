from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string, get_template

from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.models import Questionario


def new(request):
    if request.method == 'POST':
        return create(request)
    return empty_form(request)


def empty_form(request):
    return render(request, 'questionarios/form_socioeconomico.html',
                  {'form': QuestionarioForm()})


def detalhe(request, hashid):
    try:
        questionario = Questionario.objects.get(hashId=hashid)
    except Questionario.DoesNotExist:
        raise Http404

    return render(request, 'questionarios/detalhes.html',
                  {'quest': questionario})


def create(request):
    # Recebe os dados do formulário
    form = QuestionarioForm(request.POST)

    # import ipdb
    #
    # ipdb.set_trace()
    if not form.is_valid():
        return render(request, 'questionarios/form_socioeconomico.html',
                      {'form': form})

    quest = form.save()



    _send_mail('Questionário Socioeconômico preenchido com sucesso',
               'pescar.gt.ss@gmail.com',
               quest.email,
               'questionarios/questionario_email.txt',
               {'quest': quest}
               )

    return HttpResponseRedirect(r('questionarios:detalhe', str(quest.hashId)))


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    template_html = 'questionarios/detalhes-email.html'
    html = get_template(template_html)
    html_content = html.render(context)

    # mail.send_mail(subject,
    #                body,
    #                from_,
    #                [to],
    #                html_message=msg_html,
    #                )

    msg = EmailMultiAlternatives(subject, body, from_, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()



