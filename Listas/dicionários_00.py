alien_zero = {'color': 'green', 'points': 5}
print(alien_zero)
alien_zero['x_position'] = 0  # adiciona no dicionário;
alien_zero['y_position'] = 25  # adiciona no dicionário;
print(alien_zero)
alien_zero['color'] = 'blue'  # modifica um valor do dicionário;
print(alien_zero)
alien_zero['speed'] = 'medium'
del alien_zero['points']  # remove um par chave-valor de forma permanente;
print(alien_zero)
favorite_languages = {
    'Pedro': 'ruby',
    'Thulio': 'rust',
    'JP': 'C#',
    'Matheus': 'python',
    'Erick': 'java'
}
print(f"Erick's favorite language is {favorite_languages['Erick'].title()}")
person = {'first_name': 'Matheus', 'last_name': 'Gomes', 'age': 25, 'city': 'Franca/SP'}
print(f"Hi, my first name is {person['first_name']}\nmy last name is {person['last_name']}\n"
      f"I'm {person['age']} years old and I live in {person['city']}")
