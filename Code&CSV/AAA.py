import csv
import random
from faker import Faker # necessário "pip install faker" no terminal

fake = Faker()

def generate_pacientes(num):
    pacientes = []
    for i in range(1, num + 1):
        pacientes.append({
            "ID_Paciente": i,
            "Nome": fake.name(),
            "Data_Nascimento": fake.date_of_birth(minimum_age=1, maximum_age=100).strftime('%Y-%m-%d'),
            "Sexo": random.choice(["Masculino", "Feminino"]),
            "Endereco": fake.address().replace("\n", ", "),
            "Contato": fake.phone_number()
        })
    return pacientes

def generate_medicos(num):
    medicos = []
    especialidades = ["Cardiologia", "Neurologia", "Ortopedia", "Pediatria", "Dermatologia"]
    for i in range(1, num + 1):
        medicos.append({
            "ID_Medico": i,
            "Nome": fake.name(),
            "Especialidade": random.choice(especialidades),
            "Registro_CRN": fake.unique.numerify("CRN-#####")
        })
    return medicos

def generate_diagnosticos(num):
    diagnosticos = []
    categorias = ["Infeccioso", "Genético", "Metabólico", "Cardíaco", "Neurológico"]
    for i in range(1, num + 1):
        diagnosticos.append({
            "ID_Diagnostico": i,
            "Descricao": fake.sentence(nb_words=6),
            "Categoria": random.choice(categorias)
        })
    return diagnosticos

def generate_medicamentos(num):
    medicamentos = []
    tipos = ["Comprimido", "Xarope", "Injeção", "Pomada", "Cápsula"]
    for i in range(1, num + 1):
        medicamentos.append({
            "ID_Medicamento": i,
            "Nome": fake.word().capitalize(),
            "Tipo": random.choice(tipos),
            "Dosagem": f"{random.randint(1, 500)}mg"
        })
    return medicamentos

def generate_consultas(num, pacientes, medicos, diagnosticos):
    consultas = []
    for i in range(1, num + 1):
        consultas.append({
            "ID_Consulta": i,
            "ID_Paciente": random.choice(pacientes)["ID_Paciente"],
            "Data_Consulta": fake.date_this_year().strftime('%Y-%m-%d'),
            "Medico_Responsavel": random.choice(medicos)["ID_Medico"],
            "Diagnostico": random.choice(diagnosticos)["ID_Diagnostico"],
            "Tratamento_Prescrito": fake.sentence(nb_words=8)
        })
    return consultas

def generate_prescricoes(num, consultas, medicamentos):
    prescricoes = []
    for i in range(1, num + 1):
        prescricoes.append({
            "ID_Prescricao": i,
            "ID_Consulta": random.choice(consultas)["ID_Consulta"],
            "ID_Medicamento": random.choice(medicamentos)["ID_Medicamento"],
            "Quantidade": random.randint(1, 10),
            "Instrucoes": fake.sentence(nb_words=5)
        })
    return prescricoes

def write_csv(filename, fieldnames, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Quantas linhas quero
num_entries  = 10000
pacientes    = generate_pacientes(num_entries)
medicos      = generate_medicos(num_entries)
diagnosticos = generate_diagnosticos(num_entries)
medicamentos = generate_medicamentos(num_entries)
consultas    = generate_consultas(num_entries, pacientes, medicos, diagnosticos)
prescricoes  = generate_prescricoes(num_entries, consultas, medicamentos)

# Passando os dados para csv
write_csv("Pacientes.csv", ["ID_Paciente", "Nome", "Data_Nascimento", "Sexo", "Endereco", "Contato"], pacientes)
write_csv("Medicos.csv", ["ID_Medico", "Nome", "Especialidade", "Registro_CRN"], medicos)
write_csv("Diagnosticos.csv", ["ID_Diagnostico", "Descricao", "Categoria"], diagnosticos)
write_csv("Medicamentos.csv", ["ID_Medicamento", "Nome", "Tipo", "Dosagem"], medicamentos)
write_csv("Consultas.csv", ["ID_Consulta", "ID_Paciente", "Data_Consulta", "Medico_Responsavel", "Diagnostico", "Tratamento_Prescrito"], consultas)
write_csv("Prescricoes.csv", ["ID_Prescricao", "ID_Consulta", "ID_Medicamento", "Quantidade", "Instrucoes"], prescricoes)

# Após a execução, pode demorar alguns segundos paras os arquivos serem gerados