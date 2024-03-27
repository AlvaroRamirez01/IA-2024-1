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
		if (inicio == null || final == null)
		{
			return false;
		}

		List<Vertice> open = new List<Vertice>();
		List<Vertice> closed = new List<Vertice>();

		inicio.g = 0;
		inicio.h = distancia(inicio,final);
		inicio.f = inicio.h;

		open.Add(inicio);
		
		while (open.Count > 0)
		{
			int i = menorF(open);
			Vertice actual = open[i];
			if (actual.id == final.id)
			{
				reconstruirCamino(inicio,final);
				return true;
			}
			open.RemoveAt(i);
			closed.Add(actual);

			foreach (Vertice v in actual.vecinos)
			{
				if (closed.IndexOf(v) > -1)
				{
					continue;
				}
				if (open.IndexOf(v) == -1)
				{
					open.Add(v);
					v.camino = actual;
					v.g = actual.g + 1;
					v.h = distancia(actual, final);
					v.f = v.g + v.h;
				}
			}
		}
		return true;
    }

	//Auxiliar que reconstruye el camino de A*
	public void reconstruirCamino(Vertice inicio, Vertice final) {
		camino.Clear();
		camino.Add(final);
		//Completar
		var p = final.camino;
		while (p.id != inicio.id)
		{
			camino.Insert(0, p);
			p = p.camino;
		}
		camino.Insert(0, inicio);
		string aux = "";
		foreach (Vertice v in camino)
		{
			aux += v.id.ToString() + ",";
		}
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
