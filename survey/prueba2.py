import json
def calculate_survey_score(answers):
    answers=json.loads(answers)
    answers=list(answers.values())

lista = SurveyResponse.objects.filter(user=req.user)

for element in lista:

    element.questions = json.loads(element.questions)

    respuesta_1_puntaje = element.questions.question_1.value
    respuesta_2_puntaje = element.questions.question_2.value
    respuesta_3_puntaje = element.questions.question_3.value
    respuesta_4_puntaje = element.questions.question_4.value
    respuesta_5_puntaje = element.questions.question_5.value
    respuesta_6_puntaje = element.questions.question_6.value
    respuesta_7_puntaje = element.questions.question_7.value
    respuesta_8_puntaje = element.questions.question_8.value
    respuesta_9_puntaje = element.questions.question_9.value
    respuesta_10_puntaje = element.questions.question_10.value
    respuesta_11_puntaje = element.questions.question_11.value
    respuesta_12_puntaje = element.questions.question_12.value
    respuesta_13_puntaje = element.questions.question_13.value
    respuesta_14_puntaje = element.questions.question_14.value
    respuesta_15_puntaje = element.questions.question_15.value
    respuesta_16_puntaje = element.questions.question_16.value
    respuesta_17_puntaje = element.questions.question_17.value
    respuesta_18_puntaje = element.questions.question_18.value
    respuesta_19_puntaje = element.questions.question_19.value
    respuesta_20_puntaje = element.questions.question_20.value
    respuesta_21_puntaje = element.questions.question_21.value
    respuesta_22_puntaje = element.questions.question_22.value
    respuesta_23_puntaje = element.questions.question_23.value
    respuesta_24_puntaje = element.questions.question_24.value
    respuesta_25_puntaje = element.questions.question_25.value
    respuesta_26_puntaje = element.questions.question_26.value
    respuesta_27_puntaje = element.questions.question_27.value
    respuesta_28_puntaje = element.questions.question_28.value
    respuesta_29_puntaje = element.questions.question_29.value
    respuesta_30_puntaje = element.questions.question_30.value
    respuesta_31_puntaje = element.questions.question_31.value
    respuesta_32_puntaje = element.questions.question_32.value
    respuesta_33_puntaje = element.questions.question_33.value
    respuesta_34_puntaje = element.questions.question_34.value
    respuesta_35_puntaje = element.questions.question_35.value
    respuesta_36_puntaje = element.questions.question_36.value
    respuesta_37_puntaje = element.questions.question_37.value
    respuesta_38_puntaje = element.questions.question_38.value
    respuesta_39_puntaje = element.questions.question_39.value
    respuesta_40_puntaje = element.questions.question_40.value
    respuesta_41_puntaje = element.questions.question_41.value
    respuesta_42_puntaje = element.questions.question_42.value
    respuesta_43_puntaje = element.questions.question_43.value
    respuesta_44_puntaje = element.questions.question_44.value
    respuesta_45_puntaje = element.questions.question_45.value
    respuesta_46_puntaje = element.questions.question_46.value
    respuesta_47_puntaje = element.questions.question_47.value
    respuesta_48_puntaje = element.questions.question_48.value
    respuesta_49_puntaje = element.questions.question_49.value
    respuesta_50_puntaje = element.questions.question_50.value
    respuesta_51_puntaje = element.questions.question_51.value

    #puntajes por sección
    puntaje_total_seccion_1 = (respuesta_1_puntaje + respuesta_2_puntaje+ respuesta_3_puntaje+ respuesta_4_puntaje+ respuesta_5_puntaje) / 5
    puntaje_total_seccion_2 =  (respuesta_6_puntaje+ respuesta_7_puntaje + respuesta_8_puntaje+respuesta_9_puntaje+ respuesta_10_puntaje+ respuesta_11_puntaje) / 6
    puntaje_total_seccion_3 =  (respuesta_12_puntaje+ respuesta_13_puntaje + respuesta_14_puntaje+ respuesta_15_puntaje+ respuesta_16_puntaje+ respuesta_17_puntaje+ respuesta_18_puntaje+ respuesta_19_puntaje) / 8
    puntaje_total_seccion_4 =  (respuesta_20_puntaje+ respuesta_21_puntaje + respuesta_22_puntaje+ respuesta_23_puntaje+ respuesta_24_puntaje+ respuesta_25_puntaje+ respuesta_26_puntaje+ respuesta_27_puntaje) / 8
    puntaje_total_seccion_5 = respuesta_28_puntaje+ respuesta_29_puntaje + respuesta_30_puntaje+ respuesta_31_puntaje+ respuesta_32_puntaje+ respuesta_33_puntaje+ respuesta_34_puntaje+ respuesta_35_puntaje) / 8
    puntaje_total_seccion_6 =  respuesta_36_puntaje+ respuesta_37_puntaje + respuesta_38_puntaje+ respuesta_39_puntaje+ respuesta_40_puntaje+ respuesta_41_puntaje+ respuesta_42_puntaje+ respuesta_43_puntaje) / 8
    puntaje_total_seccion_7 = respuesta_44_puntaje+ respuesta_45_puntaje + respuesta_46_puntaje+ respuesta_47_puntaje+ respuesta_48_puntaje+ respuesta_49_puntaje+ respuesta_50_puntaje+ respuesta_51_puntaje) / 8

    # indice global ( resultado de 1 a 5)
    puntaje_total = [(puntaje_total_seccion_1 * 0.15)+ (puntaje_total_seccion_2 *0.10)+ (puntaje_total_seccion_3 * 0.25)+(puntaje_total_seccion_4 * 0.15)+ (puntaje_total_seccion_5*0.15)+ (puntaje_total_seccion_6* 0.10)+ (puntaje_total_seccion_7 * 0.10)]

    #perdida estimada
    if 5<=puntaje_total<=4.6:
        mensaje = "La perdida estimada de energía es del 5%"
    elif 4<=puntaje_total<=4.5:
        mensaje ="La perdida estimada de energía es del 6%"
    elif 3<=puntaje_total<=3.9:
        mensaje ="La perdida estimada de energía es del 7% al 8%"
    elif 2<=puntaje_total<=2.9:
        mensaje = "La perdida estimada de energía es del 9% al 10%"
    else:
        mensaje ="La perdida estimada de energía es del 11% o más"

    return mensaje