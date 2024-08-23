def division(numerateur, denominateur):
    try:
        resultat = numerateur / denominateur
        raise NameError("Mauvais nom!!!!!")

    except Exception as e:
        print(e)
        resultat = None
    except NameError as e:
        print("La variable numerateur ou denominateur n'a pas été définie.", e)
        resultat = None
    except TypeError:
        print("Type incompatible avec la division.")
        resultat = None
    except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")
        resultat = 0

    return resultat


if __name__ == "__main__":
    print(division(5, 2))
