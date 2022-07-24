cars_data2 = read_and_change(PATH)
clean_data = feature_engineering(cars_data2)

if __name__ == "__main__":
    print("HASIL WRANGLING")
    print(clean_data)
