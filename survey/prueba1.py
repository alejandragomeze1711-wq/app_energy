import json

from survey.questions_recommendations import questions_recommendations
def calculate_survey_score(answers):
  
    answers=list(answers.values())

    survey_answers = [None]
    for index, answer in enumerate(answers):
            survey_answers.append(answer["value"])
    print (len(survey_answers))
    print (survey_answers[0])

    puntaje_seccion_1 = (survey_answers[1] + survey_answers[2] + survey_answers[3] + survey_answers[4] + survey_answers[5])/5
    puntaje_seccion_2 =(survey_answers[6]+survey_answers[7] + survey_answers[8] + survey_answers[9] + survey_answers[10]+survey_answers[11])/6
    puntaje_seccion_3 =(survey_answers[12]+survey_answers[13] + survey_answers[14] + survey_answers[15] + survey_answers[16]+survey_answers[17]+ survey_answers[18]+survey_answers[19])/8
    puntaje_seccion_4 =(survey_answers[20]+survey_answers[21] + survey_answers[22] + survey_answers[23] + survey_answers[24]+survey_answers[25]+ survey_answers[26]+survey_answers[27])/8
    puntaje_seccion_5 =(survey_answers[28]+survey_answers[29] + survey_answers[30] + survey_answers[31] + survey_answers[32]+survey_answers[33]+ survey_answers[34]+survey_answers[35])/8
    puntaje_seccion_6 =(survey_answers[36]+survey_answers[37]+survey_answers[38] + survey_answers[39] + survey_answers[40] + survey_answers[41]+survey_answers[42]+ survey_answers[43])/8
    puntaje_seccion_7 =(+survey_answers[44]+survey_answers[45]+survey_answers[46] + survey_answers[47] + survey_answers[48] + survey_answers[49]+survey_answers[50]+ survey_answers[51])/8

    # indice global ( resultado de 1 a 5)
    puntaje_total = (puntaje_seccion_1 * 0.15)+ (puntaje_seccion_2 *0.10)+ (puntaje_seccion_3 * 0.25)+(puntaje_seccion_4 * 0.15)+ (puntaje_seccion_5*0.15)+ (puntaje_seccion_6* 0.10)+ (puntaje_seccion_7 * 0.10)


    # Determinar mensaje según el rango
    if 4.6 <= puntaje_total <= 5:
        mensaje = "La pérdida estimada de energía es del 5%."
    elif 4.0 <= puntaje_total < 4.6:
        mensaje = "La pérdida estimada de energía es del 6%."
    elif 3.0 <= puntaje_total < 4.0:
        mensaje = "La pérdida estimada de energía es del 7% al 8%."
    elif 2.0 <= puntaje_total < 3.0:
        mensaje = "La pérdida estimada de energía es del 9% al 10%."
    else:
        mensaje = "La pérdida estimada de energía es del 11% o más."

    return mensaje

def get_recommendation(question, answer):
    try:
        return questions_recommendations[question][str(answer)]
    except KeyError:
        return""
