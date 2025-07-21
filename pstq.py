import streamlit as st


def main():
    st.title("🇨🇦 Calculadora de Pontos - Imigração Quebec (PSTQ)")
    st.write("Sistema de pontuação para o Programa de Seleção dos Trabalhadores Qualificados")
    st.write("---")

    # Estado para acompanhamento dos pontos
    total_points = 0

    # Verificar se tem cônjuge
    st.subheader("📋 Informações Gerais")
    has_spouse = st.selectbox("Tem cônjuge ou companheiro(a) que o acompanha?", ["Não", "Sim"])
    is_with_spouse = has_spouse == "Sim"

    st.write("---")

    # CAPITAL HUMANO (Máximo 520 pontos)
    st.header("👤 CAPITAL HUMANO (Máximo: 520 pontos)")

    # a. Conhecimento do francês
    st.subheader("🇫🇷 a. Conhecimento do Francês")

    # Tabelas de pontuação para francês
    french_points = {
        "1-4": 0, "5-6": 38 if not is_with_spouse else 30,
        "7-8": 44 if not is_with_spouse else 35,
        "9-10": 50 if not is_with_spouse else 40,
        "11-12": 50 if not is_with_spouse else 40
    }

    levels = ["1-4", "5-6", "7-8", "9-10", "11-12"]

    col1, col2 = st.columns(2)
    with col1:
        oral_comp = st.selectbox("Nível de Compreensão Oral", levels, key="oral_comp")
        oral_prod = st.selectbox("Nível de Produção Oral", levels, key="oral_prod")

    with col2:
        written_comp = st.selectbox("Nível de Compreensão Escrita", levels, key="written_comp")
        written_prod = st.selectbox("Nível de Produção Escrita", levels, key="written_prod")

    french_total = (french_points[oral_comp] + french_points[oral_prod] +
                    french_points[written_comp] + french_points[written_prod])

    st.info(f"Pontos por Francês: {french_total}")
    total_points += french_total

    # b. Idade
    st.subheader("🎂 b. Idade")
    age = st.number_input("Idade do candidato principal", min_value=16, max_value=70, value=30)

    age_points_single = {
        range(18, 20): 110, range(20, 31): 120, 31: 110, 32: 100, 33: 90,
        34: 80, 35: 75, 36: 70, 37: 65, 38: 60, 39: 55, 40: 50,
        41: 40, 42: 30, 43: 20, 44: 10
    }

    age_points_with_spouse = {
        range(18, 20): 90, range(20, 31): 100, 31: 95, 32: 90, 33: 81,
        34: 72, 35: 68, 36: 63, 37: 59, 38: 54, 39: 50, 40: 45,
        41: 36, 42: 27, 43: 18, 44: 9
    }

    age_points = 0
    points_dict = age_points_with_spouse if is_with_spouse else age_points_single

    for age_range, points in points_dict.items():
        if isinstance(age_range, range) and age in age_range:
            age_points = points
            break
        elif isinstance(age_range, int) and age == age_range:
            age_points = points
            break

    if age >= 45:
        age_points = 0

    st.info(f"Pontos por Idade: {age_points}")
    total_points += age_points

    # c. Experiência de trabalho
    st.subheader("💼 c. Duração da Experiência de Trabalho")
    work_exp = st.selectbox("Duração da experiência de trabalho (nos últimos 5 anos)",
                            ["Menos de 12 meses", "12-23 meses", "24-35 meses", "36-47 meses", "48+ meses"])

    work_exp_points = {
        "Menos de 12 meses": 0,
        "12-23 meses": 20 if not is_with_spouse else 15,
        "24-35 meses": 40 if not is_with_spouse else 30,
        "36-47 meses": 50 if not is_with_spouse else 35,
        "48+ meses": 70 if not is_with_spouse else 50
    }

    work_points = work_exp_points[work_exp]
    st.info(f"Pontos por Experiência de Trabalho: {work_points}")
    total_points += work_points

    # d. Nível de escolaridade
    st.subheader("🎓 d. Nível de Escolaridade")
    education_options = [
        "Secundário geral completo",
        "Secundário profissional 600-899h (Quebec)",
        "Secundário profissional 900h+ (Quebec)",
        "Secundário profissional 1+ ano (fora Quebec)",
        "Pós-secundário geral 2 anos",
        "Pós-secundário técnico 900h+ (Quebec)",
        "Pós-secundário técnico 1-2 anos (fora Quebec)",
        "Pós-secundário técnico 3 anos",
        "Universitário 1º ciclo 1 ano",
        "Universitário 1º ciclo 2 anos",
        "Universitário 1º ciclo 3-4 anos",
        "Universitário 1º ciclo 5+ anos",
        "Universitário 2º ciclo 1 ano",
        "Universitário 2º ciclo 2+ anos",
        "Universitário especialização médica 2+ anos",
        "Universitário 3º ciclo"
    ]

    education = st.selectbox("Nível de escolaridade mais alto", education_options)

    education_points_single = {
        "Secundário geral completo": 13,
        "Secundário profissional 600-899h (Quebec)": 13,
        "Secundário profissional 900h+ (Quebec)": 26,
        "Secundário profissional 1+ ano (fora Quebec)": 26,
        "Pós-secundário geral 2 anos": 39,
        "Pós-secundário técnico 900h+ (Quebec)": 52,
        "Pós-secundário técnico 1-2 anos (fora Quebec)": 52,
        "Pós-secundário técnico 3 anos": 78,
        "Universitário 1º ciclo 1 ano": 78,
        "Universitário 1º ciclo 2 anos": 91,
        "Universitário 1º ciclo 3-4 anos": 104,
        "Universitário 1º ciclo 5+ anos": 110,
        "Universitário 2º ciclo 1 ano": 110,
        "Universitário 2º ciclo 2+ anos": 117,
        "Universitário especialização médica 2+ anos": 130,
        "Universitário 3º ciclo": 130
    }

    education_points_with_spouse = {
        "Secundário geral completo": 11,
        "Secundário profissional 600-899h (Quebec)": 11,
        "Secundário profissional 900h+ (Quebec)": 22,
        "Secundário profissional 1+ ano (fora Quebec)": 22,
        "Pós-secundário geral 2 anos": 33,
        "Pós-secundário técnico 900h+ (Quebec)": 44,
        "Pós-secundário técnico 1-2 anos (fora Quebec)": 44,
        "Pós-secundário técnico 3 anos": 66,
        "Universitário 1º ciclo 1 ano": 66,
        "Universitário 1º ciclo 2 anos": 77,
        "Universitário 1º ciclo 3-4 anos": 88,
        "Universitário 1º ciclo 5+ anos": 93,
        "Universitário 2º ciclo 1 ano": 93,
        "Universitário 2º ciclo 2+ anos": 99,
        "Universitário especialização médica 2+ anos": 110,
        "Universitário 3º ciclo": 110
    }

    ed_points = education_points_with_spouse[education] if is_with_spouse else education_points_single[education]
    st.info(f"Pontos por Escolaridade: {ed_points}")
    total_points += ed_points

    st.success(f"**TOTAL CAPITAL HUMANO: {french_total + age_points + work_points + ed_points} pontos**")

    st.write("---")

    # RESPOSTA ÀS NECESSIDADES DO QUEBEC (Máximo 700 pontos)
    st.header("🏢 RESPOSTA ÀS NECESSIDADES DO QUEBEC (Máximo: 700 pontos)")

    # a. Diagnóstico de mão de obra
    st.subheader("📊 a. Diagnóstico de Mão de Obra e Experiência na Profissão")
    diagnosis = st.selectbox("Diagnóstico da profissão principal",
                             ["Equilíbrio ou sem diagnóstico", "Ligeiro déficit", "Déficit"])

    prof_exp = st.selectbox("Experiência na profissão (últimos 5 anos)",
                            ["Menos de 12 meses", "12-23 meses", "24-35 meses", "36-47 meses", "48-60 meses"])

    diagnosis_points = {
        ("Equilíbrio ou sem diagnóstico", "Menos de 12 meses"): 0,
        ("Equilíbrio ou sem diagnóstico", "12-23 meses"): 5,
        ("Equilíbrio ou sem diagnóstico", "24-35 meses"): 10,
        ("Equilíbrio ou sem diagnóstico", "36-47 meses"): 15,
        ("Equilíbrio ou sem diagnóstico", "48-60 meses"): 25,
        ("Ligeiro déficit", "Menos de 12 meses"): 0,
        ("Ligeiro déficit", "12-23 meses"): 70,
        ("Ligeiro déficit", "24-35 meses"): 80,
        ("Ligeiro déficit", "36-47 meses"): 90,
        ("Ligeiro déficit", "48-60 meses"): 100,
        ("Déficit", "Menos de 12 meses"): 0,
        ("Déficit", "12-23 meses"): 90,
        ("Déficit", "24-35 meses"): 100,
        ("Déficit", "36-47 meses"): 110,
        ("Déficit", "48-60 meses"): 120
    }

    diag_points = diagnosis_points[(diagnosis, prof_exp)]
    st.info(f"Pontos por Diagnóstico de Mão de Obra: {diag_points}")
    total_points += diag_points

    # b. Diploma do Quebec
    st.subheader("🎓 b. Diploma do Quebec")
    has_quebec_diploma = st.selectbox("Possui diploma do Quebec?", ["Não", "Sim"])

    quebec_points = 0
    if has_quebec_diploma == "Sim":
        quebec_diploma = st.selectbox("Tipo de diploma do Quebec", education_options)

        quebec_diploma_points = {
            "Secundário geral completo": 20,
            "Secundário profissional 600-899h (Quebec)": 20,
            "Secundário profissional 900h+ (Quebec)": 40,
            "Pós-secundário geral 2 anos": 60,
            "Pós-secundário técnico 900h+ (Quebec)": 80,
            "Pós-secundário técnico 3 anos": 120,
            "Universitário 1º ciclo 1 ano": 120,
            "Universitário 1º ciclo 2 anos": 140,
            "Universitário 1º ciclo 3-4 anos": 160,
            "Universitário 1º ciclo 5+ anos": 170,
            "Universitário 2º ciclo 1 ano": 170,
            "Universitário 2º ciclo 2+ anos": 180,
            "Universitário especialização médica 2+ anos": 200,
            "Universitário 3º ciclo": 200
        }

        quebec_points = quebec_diploma_points.get(quebec_diploma, 0)

    st.info(f"Pontos por Diploma do Quebec: {quebec_points}")
    total_points += quebec_points

    # c. Experiência de trabalho no Quebec
    st.subheader("🍁 c. Experiência de Trabalho no Quebec")
    quebec_work = st.selectbox("Experiência de trabalho no Quebec (últimos 5 anos)",
                               ["Menos de 12 meses", "12-23 meses", "24-35 meses", "36-47 meses", "48-60 meses"])

    quebec_work_points = {
        "Menos de 12 meses": 0,
        "12-23 meses": 40,
        "24-35 meses": 80,
        "36-47 meses": 120,
        "48-60 meses": 160
    }

    qc_work_points = quebec_work_points[quebec_work]
    st.info(f"Pontos por Experiência no Quebec: {qc_work_points}")
    total_points += qc_work_points

    # d. Permanência fora de Montreal
    st.subheader("🏘️ d. Permanência fora da Região Metropolitana de Montreal")

    col1, col2, col3 = st.columns(3)

    with col1:
        residence_outside = st.selectbox("Duração da residência fora de Montreal",
                                         ["0-5 meses", "6-11 meses", "12-23 meses", "24-35 meses", "36-47 meses",
                                          "48+ meses"])

    with col2:
        work_outside = st.selectbox("Duração do trabalho fora de Montreal",
                                    ["0-5 meses", "6-11 meses", "12-23 meses", "24-35 meses", "36-47 meses",
                                     "48+ meses"])

    with col3:
        study_outside = st.selectbox("Duração dos estudos fora de Montreal",
                                     ["0-5 meses", "6-11 meses", "12-23 meses", "24-35 meses", "36-47 meses",
                                      "48+ meses"])

    residence_points = {"0-5 meses": 0, "6-11 meses": 6, "12-23 meses": 16, "24-35 meses": 24, "36-47 meses": 32,
                        "48+ meses": 40}
    work_outside_points = {"0-5 meses": 0, "6-11 meses": 9, "12-23 meses": 24, "24-35 meses": 36, "36-47 meses": 48,
                           "48+ meses": 60}
    study_outside_points = {"0-5 meses": 0, "6-11 meses": 3, "12-23 meses": 8, "24-35 meses": 12, "36-47 meses": 16,
                            "48+ meses": 20}

    outside_montreal_points = (residence_points[residence_outside] +
                               work_outside_points[work_outside] +
                               study_outside_points[study_outside])

    st.info(f"Pontos por Permanência fora de Montreal: {outside_montreal_points}")
    total_points += outside_montreal_points

    # e. Oferta de emprego validada
    st.subheader("💼 e. Oferta de Emprego Validada")
    job_offer = st.selectbox("Possui oferta de emprego validada?", ["Não", "Sim"])

    job_offer_points = 0
    if job_offer == "Sim":
        job_location = st.selectbox("Localização do emprego",
                                    ["Dentro da Região Metropolitana de Montreal",
                                     "Fora da Região Metropolitana de Montreal"])
        job_offer_points = 30 if job_location == "Dentro da Região Metropolitana de Montreal" else 50

    st.info(f"Pontos por Oferta de Emprego: {job_offer_points}")
    total_points += job_offer_points

    # f. Autorização para exercer profissão
    st.subheader("⚖️ f. Autorização para Exercer Profissão")
    professional_auth = st.selectbox("Possui autorização/reconhecimento profissional no Quebec?", ["Não", "Sim"])

    auth_points = 50 if professional_auth == "Sim" else 0
    st.info(f"Pontos por Autorização Profissional: {auth_points}")
    total_points += auth_points

    quebec_total = diag_points + quebec_points + qc_work_points + outside_montreal_points + job_offer_points + auth_points
    st.success(f"**TOTAL NECESSIDADES DO QUEBEC: {quebec_total} pontos**")

    st.write("---")

    # FATORES DE ADAPTAÇÃO (Máximo 180 pontos)
    st.header("🏠 FATORES DE ADAPTAÇÃO (Máximo: 180 pontos)")

    adaptation_total = 0

    # a. Estudos sem diploma no Quebec
    st.subheader("📚 a. Estudos sem Diploma no Quebec")
    quebec_studies = st.selectbox("Estudos no Quebec (sem obter diploma)",
                                  ["Nenhum", "Terminado", "Em curso"])

    study_points = 0
    if quebec_studies != "Nenhum":
        study_duration = st.selectbox("Duração dos estudos",
                                      ["Menos de 6 meses", "6-11 meses", "12-23 meses", "24-35 meses", "36-47 meses",
                                       "48+ meses"])

        if quebec_studies == "Terminado":
            study_points_dict = {"Menos de 6 meses": 0, "6-11 meses": 1, "12-23 meses": 3, "24-35 meses": 5,
                                 "36-47 meses": 8, "48+ meses": 10}
        else:  # Em curso
            study_points_dict = {"Menos de 6 meses": 0, "6-11 meses": 5, "12-23 meses": 12, "24-35 meses": 18,
                                 "36-47 meses": 24, "48+ meses": 30}

        study_points = study_points_dict[study_duration]

    st.info(f"Pontos por Estudos no Quebec: {study_points}")
    adaptation_total += study_points

    # b. Membro da família no Quebec
    st.subheader("👨‍👩‍👧‍👦 b. Membro da Família no Quebec")
    family_quebec = st.selectbox("Tem familiar no Quebec?",
                                 ["Não", "Sim - ligado ao candidato", "Sim - ligado ao cônjuge"])

    family_points = {"Não": 0, "Sim - ligado ao candidato": 10, "Sim - ligado ao cônjuge": 5}
    family_pts = family_points[family_quebec]

    st.info(f"Pontos por Família no Quebec: {family_pts}")
    adaptation_total += family_pts

    # Pontos do cônjuge (se aplicável)
    spouse_total = 0
    if is_with_spouse:
        st.subheader("💑 Informações do Cônjuge/Companheiro(a)")

        # Francês do cônjuge
        st.write("**Conhecimento do Francês do Cônjuge**")
        col1, col2 = st.columns(2)
        with col1:
            spouse_oral_comp = st.selectbox("Compreensão Oral - Cônjuge", ["1-3", "4", "5-6", "7-8", "9-10", "11-12"],
                                            key="sp_oral_comp")
            spouse_oral_prod = st.selectbox("Produção Oral - Cônjuge", ["1-3", "4", "5-6", "7-8", "9-10", "11-12"],
                                            key="sp_oral_prod")

        with col2:
            spouse_written_comp = st.selectbox("Compreensão Escrita - Cônjuge",
                                               ["1-3", "4", "5-6", "7-8", "9-10", "11-12"], key="sp_written_comp")
            spouse_written_prod = st.selectbox("Produção Escrita - Cônjuge",
                                               ["1-3", "4", "5-6", "7-8", "9-10", "11-12"], key="sp_written_prod")

        spouse_french_points = {"1-3": 0, "4": 4, "5-6": 6, "7-8": 8, "9-10": 10, "11-12": 10}
        spouse_french_total = (spouse_french_points[spouse_oral_comp] + spouse_french_points[spouse_oral_prod] +
                               spouse_french_points[spouse_written_comp] + spouse_french_points[spouse_written_prod])

        # Idade do cônjuge
        spouse_age = st.number_input("Idade do cônjuge", min_value=16, max_value=70, value=28)

        spouse_age_points = {
            range(16, 20): 18, range(20, 31): 20, 31: 18, 32: 17, 33: 16, 34: 15, 35: 14,
            36: 12, 37: 10, 38: 8, 39: 7, 40: 6, 41: 5, 42: 4, 43: 3, 44: 2
        }

        spouse_age_pts = 0
        for age_range, points in spouse_age_points.items():
            if isinstance(age_range, range) and spouse_age in age_range:
                spouse_age_pts = points
                break
            elif isinstance(age_range, int) and spouse_age == age_range:
                spouse_age_pts = points
                break

        if spouse_age >= 45:
            spouse_age_pts = 0

        # Experiência do cônjuge no Quebec
        spouse_quebec_exp = st.selectbox("Experiência de trabalho do cônjuge no Quebec",
                                         ["0-5 meses", "6-11 meses", "12-23 meses", "24-35 meses", "36-47 meses",
                                          "48-60 meses"])

        spouse_exp_points = {"0-5 meses": 0, "6-11 meses": 5, "12-23 meses": 10, "24-35 meses": 15, "36-47 meses": 23,
                             "48-60 meses": 30}
        spouse_exp_pts = spouse_exp_points[spouse_quebec_exp]

        # Escolaridade do cônjuge
        spouse_education = st.selectbox("Escolaridade do cônjuge", education_options, key="spouse_ed")

        spouse_ed_points = {
            "Secundário geral completo": 2, "Secundário profissional 600-899h (Quebec)": 2,
            "Secundário profissional 900h+ (Quebec)": 4, "Secundário profissional 1+ ano (fora Quebec)": 4,
            "Pós-secundário geral 2 anos": 6, "Pós-secundário técnico 900h+ (Quebec)": 8,
            "Pós-secundário técnico 1-2 anos (fora Quebec)": 8, "Pós-secundário técnico 3 anos": 12,
            "Universitário 1º ciclo 1 ano": 12, "Universitário 1º ciclo 2 anos": 14,
            "Universitário 1º ciclo 3-4 anos": 16, "Universitário 1º ciclo 5+ anos": 17,
            "Universitário 2º ciclo 1 ano": 17, "Universitário 2º ciclo 2+ anos": 18,
            "Universitário especialização médica 2+ anos": 20, "Universitário 3º ciclo": 20
        }

        spouse_ed_pts = spouse_ed_points[spouse_education]

        # Diploma do Quebec do cônjuge
        spouse_quebec_diploma = st.selectbox("Cônjuge possui diploma do Quebec?", ["Não", "Sim"],
                                             key="spouse_qc_diploma")

        spouse_quebec_pts = 0
        if spouse_quebec_diploma == "Sim":
            spouse_qc_diploma_type = st.selectbox("Tipo de diploma do cônjuge", education_options, key="spouse_qc_type")

            spouse_quebec_diploma_points = {
                "Secundário geral completo": 3, "Secundário profissional 600-899h (Quebec)": 3,
                "Secundário profissional 900h+ (Quebec)": 6, "Pós-secundário geral 2 anos": 9,
                "Pós-secundário técnico 900h+ (Quebec)": 12, "Pós-secundário técnico 3 anos": 18,
                "Universitário 1º ciclo 1 ano": 18, "Universitário 1º ciclo 2 anos": 21,
                "Universitário 1º ciclo 3-4 anos": 24, "Universitário 1º ciclo 5+ anos": 25,
                "Universitário 2º ciclo 1 ano": 25, "Universitário 2º ciclo 2+ anos": 27,
                "Universitário especialização médica 2+ anos": 30, "Universitário 3º ciclo": 30
            }

            spouse_quebec_pts = spouse_quebec_diploma_points.get(spouse_qc_diploma_type, 0)

        spouse_total = spouse_french_total + spouse_age_pts + spouse_exp_pts + spouse_ed_pts + spouse_quebec_pts

        st.info(f"**Pontos do Cônjuge**: {spouse_total}")
        adaptation_total += spouse_total

    adaptation_total += study_points + family_pts
    st.success(f"**TOTAL FATORES DE ADAPTAÇÃO: {adaptation_total} pontos**")

    # PONTUAÇÃO FINAL
    st.write("---")
    st.header("🏆 PONTUAÇÃO FINAL")

    final_total = (french_total + age_points + work_points + ed_points +
                   quebec_total + adaptation_total)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Capital Humano", f"{french_total + age_points + work_points + ed_points}",
                  help="Máximo: 520 pontos")

    with col2:
        st.metric("Necessidades Quebec", f"{quebec_total}",
                  help="Máximo: 700 pontos")

    with col3:
        st.metric("Fatores de Adaptação", f"{adaptation_total}",
                  help="Máximo: 180 pontos")

    st.write("---")

    # Resultado final com cores
    if final_total >= 1000:
        st.success(f"## 🎉 PONTUAÇÃO TOTAL: {final_total} pontos")
        st.success("**Excelente pontuação! Muito competitivo para receber um convite.**")
    elif final_total >= 800:
        st.warning(f"## ⚡ PONTUAÇÃO TOTAL: {final_total} pontos")
        st.info("**Boa pontuação! Chances razoáveis de receber um convite.**")
    else:
        st.error(f"## 📊 PONTUAÇÃO TOTAL: {final_total} pontos")
        st.info("**Considere melhorar alguns critérios para aumentar suas chances.**")

    # Máximo teórico
    st.caption("**Pontuação máxima teórica**: 1.400 pontos")
    st.caption("**Documento base**: Mise à jour le 2 juillet 2025")

    st.write("---")
    st.markdown(
        "Desenvolvido por: rafael.olima@gmail.com"
    )


if __name__ == "__main__":
    main()