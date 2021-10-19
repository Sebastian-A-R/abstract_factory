from triangulofactory import TrianguloFactory

if __name__ == "__main__":

    factory = TrianguloFactory()
    triangulo = factory.createTriangulo(10, 10, 10)
    print(triangulo.getDescripcion())
    
    print("------")
    factory2 = TrianguloFactory()
    triangulo2 = factory2.createTriangulo(12, 11, 10)
    print(triangulo2.getDescripcion())
    
    print("------")
    factory3 = TrianguloFactory()
    triangulo3 = factory3.createTriangulo(10, 13, 10)
    print(triangulo3.getDescripcion())