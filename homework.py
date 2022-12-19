class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float):
        self.training_type = training_type,
        self.duration = duration,
        self.distance = distance,
        self.speed = speed,
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance, 3} км; '
                f'Ср. скорость: {self.speed, 3} км/ч; '
                f'Потрачено ккал: {round(self.calories, 3)}.')


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed: float = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self, training) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(*training)


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float):
        super().__init__(action, duration, weight)

    def get_distance(self) -> float:
        pass

    def get_mean_speed(self) -> float:
        pass

    def get_spent_calories(self) -> float:
        result: float = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() +
                         self.CALORIES_MEAN_SPEED_SHIFT) *
                         self.weight / self.M_IN_KM * self.duration)
        return result

    def show_training_info(self) -> InfoMessage:
        pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    FIRST_WEIGHT_COEFFICIENT = 0.035
    SECOND_WEIGHT_COEFFICIENT = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float):
        super().__init__(action, duration, weight)
        self.height = height

    def get_distance(self) -> float:
        pass

    def get_mean_speed(self) -> float:
        pass

    def get_spent_calories(self) -> float:
        spent_calories = ((self.FIRST_WEIGHT_COEFFICIENT * self.weight +
                          (self.get_mean_speed() ** 2 / self.height) *
                          self.SECOND_WEIGHT_COEFFICIENT * self.weight) *
                          self.duration)
        return spent_calories

    def show_training_info(self) -> InfoMessage:
        pass


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    FIRST_CAL_COEFFICIENT = 1.1
    SECOND_CAL_COEFFICIENT = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        pass

    def get_mean_speed(self) -> float:
        mean_speed: float = (self.length_pool * self.count_pool /
                             self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        spent_calories: float = ((self.get_mean_speed() + self.FIRST_CAL_COEFFICIENT) *
                                 self.SECOND_CAL_COEFFICIENT * self.weight * self.duration)
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type = {'SWM': Swimming(*data),
                     'RUN': Running(*data),
                     'WLK': SportsWalking(*data)}
    return training_type[workout_type]


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = Training.show_training_info(training)
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
