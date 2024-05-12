import matplotlib.pyplot as plt


capacity = 16000  # емкость персонального энергоблока (ПЭБ)
initCharge = 6000  # уровень заряда ПЭБ

'''Почасовая цена за электроэнергию'''
priceSchedule = [1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
                 2.0, 3.0, 5.0, 5.0, 5.0, 4.5,
                 3.0, 3.0, 3.0, 3.0, 4.5, 5.0,
                 7.0, 9.0, 11.0, 12.0, 8.0, 4.0]

'''Почасовое потребление электроэнергии'''
loadSchedule = [480, 320, 320, 360, 360, 360,
                420, 920, 1200, 720, 680, 720,
                800, 820, 960, 1200, 1380, 1380,
                1520, 1800, 1920, 1920, 1640, 1020]

constantLoad = 400  # потребитель с постоянной нагрузкой
targetCharge = 4800  # конечный заряд аккумулятора

'''Продажа/покупка электроэнергии'''
maxEnergy = 4000
minEnergy = 1000

'''Инициализация массивов хранящих уровень электроэнергии батареи и затраты на покупку энергии'''
resLevelEnergy = [0] * len(loadSchedule)
resExpenses = [0] * len(loadSchedule)

'''Словарь промежуточных данных'''
data = {
    # 'levelEnergy': resLevelEnergy,
    # 'Expenses': resExpenses
}


'''Расчет уровня заряда ПЭБ на данный час и затрат на покупку энергии'''
def calculate_simple(cons_power, index, resLevelEnergy_mass, resExpenses_mass):
    global initCharge
    global targetCharge

    res_energy = 0
    if targetCharge > (initCharge - cons_power - constantLoad):
        # Покупка электроэнергии
        if cons_power % minEnergy != 0:
            res_energy = (cons_power / minEnergy) * 1000 + 1000
        else:
            res_energy = (cons_power / minEnergy) * 1000

        initCharge = initCharge + res_energy - cons_power - constantLoad
    else:
        initCharge = initCharge - cons_power - constantLoad
    # Запись результатов шага рачсета
    resLevelEnergy_mass[index] = initCharge
    resExpenses_mass[index] = -res_energy * priceSchedule[index]


'''Визуализация расчетов'''
def visual_calculate_simple(time_list, energy_list, gold_list):
    fig, ax = plt.subplots(nrows=1, ncols=2)

    fig.set_figheight(10)
    fig.set_figwidth(20)

    ax[0].plot(time_list, energy_list, c='orange')
    ax[1].plot(time_list, gold_list, c='red')

    ax[0].axis(xmin=0, xmax=25, ymin=0, ymax=16000)
    ax[1].axis(xmin=0, xmax=25, ymin=0, ymax=-50000)

    ax[0].set_title('levelEnergy ПЭБ')
    ax[1].set_title('Expenses')
    ax[0].set_xlabel('time, ч')
    ax[1].set_xlabel('time, ч')
    ax[0].set_ylabel('energy, кВТ*ч')
    ax[1].set_ylabel('gold, руб')

    fig.suptitle('Результаты дня без плановых торгов')
    plt.show()


'''Опыт без плановых торгов'''
def res_calculate_simple(time_list):
    # Предварительная очистка массивов
    data.clear()
    data["levelEnergy"] = resLevelEnergy
    data["Expenses"] = resExpenses

    # Расчет энергопотребления за сутки
    for i in range(len(loadSchedule)):
        calculate_simple(loadSchedule[i], i, data["levelEnergy"], data["Expenses"])

    summExpenses = 0
    for i in range(len(data["Expenses"])):
        summExpenses += data["Expenses"][i]
    print("Суммарные затраты на покупку электроэнергии: ", summExpenses)

    visual_calculate_simple(time_list, data["levelEnergy"], data["Expenses"])


'''Временная ось'''
time = []
for i in range(len(loadSchedule)):
    time.append(i + 1)


def visual_consumer(time_mass, power_mass):
    plt.figure()
    plt.title('График потребления нагрузки')
    plt.grid()
    plt.plot(time_mass, power_mass, 'tab:red')
    plt.show()

    return 0


# visual_consumer(time, loadSchedule)
res_calculate_simple(time)
