import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


def main():
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
    }

    df = pd.DataFrame(data)

    print(df)
    print("Средняя выручка:", df["Выручка"].mean())

    total_revenue = df["Выручка"].sum()
    total_cost = 300000
    profitability = calculate_profitability(total_revenue, total_cost)

    print(f"Рентабельность: {profitability:.2f}%")


if __name__ == "__main__":
    main()