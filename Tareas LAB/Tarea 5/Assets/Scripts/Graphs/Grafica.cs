using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Grafica{

    public List<Vertice> grafica = new List<Vertice>();
	public List<Vertice> camino = new List<Vertice>();

	//Agrega un v�rtice a la lista de v�rtices de la gr�fica.
    public void AgregarVertice(Vertice nuevoVertice) {
        if(!grafica.Contains(nuevoVertice)){
			grafica.Add(nuevoVertice);
		}
    }

	//Aplica el Algoritmo de A*
	public bool AStar(Vertice inicio, Vertice final) {
		//Completar
		return true;
    }

	//Auxiliar que reconstruye el camino de A*
	public void reconstruirCamino(Vertice inicio, Vertice final) {
		camino.Clear();
		camino.Add(final);
		//Completar
	}

	float distancia(Vertice a, Vertice b) {
		//Completar distancia entre dos vectores utilizando Vector3.distance()
		float dx = a.posicion.x - b.posicion.x;
		float dy = a.posicion.y - b.posicion.y;
		float dz = a.posicion.z - b.posicion.z;
		float dist = dx * dx + dy * dy + dz * dz;
		return (dist);
	}

	int menorF(List<Vertice> l) {
		//Coompletar
		float menorf = 0;
		int count = 0;
		int indice = 0;

		menorf = l[0].f;
		for (int i = 0; i < l.Count; i++)
		{
			if (l[i].f <= menorf)
			{
				menorf = l[i].f;
				indice = count;
			}
			count++;
		} 
		return indice;
	}

	//M�todo que da una representaci�n escrita de la gr�fica.
	public string toString() {
		string aux = "\nG:\n";
		foreach (Vertice v in grafica) {
			aux += v.toString() + "\n";
		}
		return aux;
	}

}
