from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from survey.prueba1 import calculate_survey_score, get_recommendation
from .models import SurveyResponse
from .questions_options import questions_options
from django.utils import timezone

#registrara facturas 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Avg
from datetime import datetime
from .models import MonthlyBill

# Create your views here.
@login_required
def survey(req):
    return render(req, "survey/survey.html")

@csrf_exempt
@login_required
def survey_post(req):
    if req.method == "POST":
        print(req.POST["question_1"])
        new_survey = SurveyResponse(user=req.user)
        new_survey.questions = {
            "question_1": {
                "text": questions_options["question_1"][int(req.POST["question_1"])]["text"],
                "value": questions_options["question_1"][int(req.POST["question_1"])]["value"]
            },
            "question_2": {
                "text": questions_options["question_2"][int(req.POST["question_2"])]["text"],
                "value": questions_options["question_2"][int(req.POST["question_2"])]["value"]
            },
            "question_3": {
                "text": questions_options["question_3"][int(req.POST["question_3"])]["text"],
                "value": questions_options["question_3"][int(req.POST["question_3"])]["value"]
            },
            "question_4": {
                "text": questions_options["question_4"][int(req.POST["question_4"])]["text"],
                "value": questions_options["question_4"][int(req.POST["question_4"])]["value"]
            },
            "question_5": {
                "text": questions_options["question_5"][int(req.POST["question_5"])]["text"],
                "value": questions_options["question_5"][int(req.POST["question_5"])]["value"]
            },
            "question_6": {
                "text": questions_options["question_6"][int(req.POST["question_6"])]["text"],
                "value": questions_options["question_6"][int(req.POST["question_6"])]["value"]
            },
            "question_7": {
                "text": questions_options["question_7"][int(req.POST["question_7"])]["text"],
                "value": questions_options["question_7"][int(req.POST["question_7"])]["value"]
            },
            "question_8": {
                "text": questions_options["question_8"][int(req.POST["question_8"])]["text"],
                "value": questions_options["question_8"][int(req.POST["question_8"])]["value"]
            },
            "question_9": {
                "text": questions_options["question_9"][int(req.POST["question_9"])]["text"],
                "value": questions_options["question_9"][int(req.POST["question_9"])]["value"]
            },
            "question_10": {
                "text": questions_options["question_10"][int(req.POST["question_10"])]["text"],
                "value": questions_options["question_10"][int(req.POST["question_10"])]["value"]
            },
            "question_11": {
                "text": questions_options["question_11"][int(req.POST["question_11"])]["text"],
                "value": questions_options["question_11"][int(req.POST["question_11"])]["value"]
            },
            "question_12": {
                "text": questions_options["question_12"][int(req.POST["question_12"])]["text"],
                "value": questions_options["question_12"][int(req.POST["question_12"])]["value"]
            },
            "question_13": {
                "text": questions_options["question_13"][int(req.POST["question_13"])]["text"],
                "value": questions_options["question_13"][int(req.POST["question_13"])]["value"]
            },
            "question_14": {
                "text": questions_options["question_14"][int(req.POST["question_14"])]["text"],
                "value": questions_options["question_14"][int(req.POST["question_14"])]["value"]
            },
            "question_15": {
                "text": questions_options["question_15"][int(req.POST["question_15"])]["text"],
                "value": questions_options["question_15"][int(req.POST["question_15"])]["value"]
            },
            "question_16": {
                "text": questions_options["question_16"][int(req.POST["question_16"])]["text"],
                "value": questions_options["question_16"][int(req.POST["question_16"])]["value"]
            },
            "question_17": {
                "text": questions_options["question_17"][int(req.POST["question_17"])]["text"],
                "value": questions_options["question_17"][int(req.POST["question_17"])]["value"]
            },
            "question_18": {
                "text": questions_options["question_18"][int(req.POST["question_18"])]["text"],
                "value": questions_options["question_18"][int(req.POST["question_18"])]["value"]
            },
            "question_19": {
                "text": questions_options["question_19"][int(req.POST["question_19"])]["text"],
                "value": questions_options["question_19"][int(req.POST["question_19"])]["value"]
            },
            "question_20": {
                "text": questions_options["question_20"][int(req.POST["question_20"])]["text"],
                "value": questions_options["question_20"][int(req.POST["question_20"])]["value"]
            },
            "question_21": {
                "text": questions_options["question_21"][int(req.POST["question_21"])]["text"],
                "value": questions_options["question_21"][int(req.POST["question_21"])]["value"]
            },
            "question_22": {
                "text": questions_options["question_22"][int(req.POST["question_22"])]["text"],
                "value": questions_options["question_22"][int(req.POST["question_22"])]["value"]
            },
            "question_23": {
                "text": questions_options["question_23"][int(req.POST["question_23"])]["text"],
                "value": questions_options["question_23"][int(req.POST["question_23"])]["value"]
            },
            "question_24": {
                "text": questions_options["question_24"][int(req.POST["question_24"])]["text"],
                "value": questions_options["question_24"][int(req.POST["question_24"])]["value"]
            },
            "question_25": {
                "text": questions_options["question_25"][int(req.POST["question_25"])]["text"],
                "value": questions_options["question_25"][int(req.POST["question_25"])]["value"]
            },
            "question_26": {
                "text": questions_options["question_26"][int(req.POST["question_26"])]["text"],
                "value": questions_options["question_26"][int(req.POST["question_26"])]["value"]
            },
            "question_27": {
                "text": questions_options["question_27"][int(req.POST["question_27"])]["text"],
                "value": questions_options["question_27"][int(req.POST["question_27"])]["value"]
            },
            "question_28": {
                "text": questions_options["question_28"][int(req.POST["question_28"])]["text"],
                "value": questions_options["question_28"][int(req.POST["question_28"])]["value"]
            },
            "question_29": {
                "text": questions_options["question_29"][int(req.POST["question_29"])]["text"],
                "value": questions_options["question_29"][int(req.POST["question_29"])]["value"]
            },
            "question_30": {
                "text": questions_options["question_30"][int(req.POST["question_30"])]["text"],
                "value": questions_options["question_30"][int(req.POST["question_30"])]["value"]
            },
            "question_31": {
                "text": questions_options["question_31"][int(req.POST["question_31"])]["text"],
                "value": questions_options["question_31"][int(req.POST["question_31"])]["value"]
            },
            "question_32": {
                "text": questions_options["question_32"][int(req.POST["question_32"])]["text"],
                "value": questions_options["question_32"][int(req.POST["question_32"])]["value"]
            },
            "question_33": {
                "text": questions_options["question_33"][int(req.POST["question_33"])]["text"],
                "value": questions_options["question_33"][int(req.POST["question_33"])]["value"]
            },
            "question_34": {
                "text": questions_options["question_34"][int(req.POST["question_34"])]["text"],
                "value": questions_options["question_34"][int(req.POST["question_34"])]["value"]
            },
            "question_35": {
                "text": questions_options["question_35"][int(req.POST["question_35"])]["text"],
                "value": questions_options["question_35"][int(req.POST["question_35"])]["value"]
            },
            "question_36": {
                "text": questions_options["question_36"][int(req.POST["question_36"])]["text"],
                "value": questions_options["question_36"][int(req.POST["question_36"])]["value"]
            },
            "question_37": {
                "text": questions_options["question_37"][int(req.POST["question_37"])]["text"],
                "value": questions_options["question_37"][int(req.POST["question_37"])]["value"]
            },
            "question_38": {
                "text": questions_options["question_38"][int(req.POST["question_38"])]["text"],
                "value": questions_options["question_38"][int(req.POST["question_38"])]["value"]
            },
            "question_39": {
                "text": questions_options["question_39"][int(req.POST["question_39"])]["text"],
                "value": questions_options["question_39"][int(req.POST["question_39"])]["value"]
            },
            "question_40": {
                "text": questions_options["question_40"][int(req.POST["question_40"])]["text"],
                "value": questions_options["question_40"][int(req.POST["question_40"])]["value"]
            },
            "question_41": {
                "text": questions_options["question_41"][int(req.POST["question_41"])]["text"],
                "value": questions_options["question_41"][int(req.POST["question_41"])]["value"]
            },
            "question_42": {
                "text": questions_options["question_42"][int(req.POST["question_42"])]["text"],
                "value": questions_options["question_42"][int(req.POST["question_42"])]["value"]
            },
            "question_43": {
                "text": questions_options["question_43"][int(req.POST["question_43"])]["text"],
                "value": questions_options["question_43"][int(req.POST["question_43"])]["value"]
            },
            "question_44": {
                "text": questions_options["question_44"][int(req.POST["question_44"])]["text"],
                "value": questions_options["question_44"][int(req.POST["question_44"])]["value"]
            },
            "question_45": {
                "text": questions_options["question_45"][int(req.POST["question_45"])]["text"],
                "value": questions_options["question_45"][int(req.POST["question_45"])]["value"]
            },
            "question_46": {
                "text": questions_options["question_46"][int(req.POST["question_46"])]["text"],
                "value": questions_options["question_46"][int(req.POST["question_46"])]["value"]
            },
            "question_47": {
                "text": questions_options["question_47"][int(req.POST["question_47"])]["text"],
                "value": questions_options["question_47"][int(req.POST["question_47"])]["value"]
            },
            "question_48": {
                "text": questions_options["question_48"][int(req.POST["question_48"])]["text"],
                "value": questions_options["question_48"][int(req.POST["question_48"])]["value"]
            },
            "question_49": {
                "text": questions_options["question_49"][int(req.POST["question_49"])]["text"],
                "value": questions_options["question_49"][int(req.POST["question_49"])]["value"]
            },
            "question_50": {
                "text": questions_options["question_50"][int(req.POST["question_50"])]["text"],
                "value": questions_options["question_50"][int(req.POST["question_50"])]["value"]
            },
            "question_51": {
                "text": questions_options["question_51"][int(req.POST["question_51"])]["text"],
                "value": questions_options["question_51"][int(req.POST["question_51"])]["value"]
            }
        }
        new_survey.save()
        
        return redirect("home")

@login_required
def history(req):
    surveys = SurveyResponse.objects.filter(user=req.user)
    for survey in surveys:
        survey.perdida_de_energia=calculate_survey_score(survey.questions)
        survey.fecha_realizacion=timezone.localtime(survey.fecha_realizacion)
    return render(req, "survey/history.html", {
        "encuestas": surveys
    })

@login_required
def history_responses(req, survey_id):
   survey = SurveyResponse.objects.get(id=survey_id)
   responses = survey.questions
   for question in responses.keys():
       responses[question]["recommendation"] = get_recommendation(question, responses[question]["value"])
   return render(req, "survey/responses.html", {
        "responses": responses
    })

@login_required
def register_bill(request):
    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount"))
            year = int(request.POST.get("year"))
            month = int(request.POST.get("month"))

            if amount <= 0:
                messages.error(request, "El valor debe ser positivo.")
            else:
                MonthlyBill.objects.update_or_create(
                    user=request.user,
                    year=year,
                    month=month,
                    defaults={'amount': amount}
                )
                messages.success(request, "Factura registrada exitosamente.")
                return redirect("register_bill")
        except (ValueError, TypeError):
            messages.error(request, "Datos inválidos. Verifica los campos.")

    # Prellenar con el mes actual
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # Generar lista de años (de 2020 a 2030)
    years = list(range(2020, 2031))

    # Generar lista de meses con nombres
    months = [
        (1, "Enero"),
        (2, "Febrero"),
        (3, "Marzo"),
        (4, "Abril"),
        (5, "Mayo"),
        (6, "Junio"),
        (7, "Julio"),
        (8, "Agosto"),
        (9, "Septiembre"),
        (10, "Octubre"),
        (11, "Noviembre"),
        (12, "Diciembre"),
    ]

    # Cargar historial del usuario
    bills = MonthlyBill.objects.filter(user=request.user).order_by('year', 'month')

    return render(request, "survey/register_bill.html", {
        "current_year": current_year,
        "current_month": current_month,
        "years": years,
        "months": months,
        "bills": bills
    })


@login_required
def bill_chart_data(request):
    # Devuelve los datos en formato JSON para la gráfica
    from django.http import JsonResponse
    bills = MonthlyBill.objects.filter(user=request.user).order_by('year', 'month')
    data = [
        {
            "x": f"{bill.year}-{bill.month:02d}",
            "y": float(bill.amount)
        }
        for bill in bills
    ]
    return JsonResponse(data, safe=False)

@login_required
def energy_calculator(request):
    return render(request, 'survey/calculator.html')