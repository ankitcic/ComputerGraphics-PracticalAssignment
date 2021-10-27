// C++ Program to implement Cyrus Beck

#include <SFML/Graphics.hpp>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;
using namespace sf;

// Function to draw a line in SFML
void drawline(RenderWindow* window, pair<int, int> p0, pair<int, int> p1)
{
	Vertex line[] = {
		Vertex(Vector2f(p0.first, p0.second)),
		Vertex(Vector2f(p1.first, p1.second))
	};
	window->draw(line, 2, Lines);
}

// Function to draw a polygon, given vertices
void drawPolygon(RenderWindow* window, pair<int, int> vertices[], int n)
{
	for (int i = 0; i < n - 1; i++)
		drawline(window, vertices[i], vertices[i + 1]);
	drawline(window, vertices[0], vertices[n - 1]);
}

// Function to take dot product
int dot(pair<int, int> p0, pair<int, int> p1)
{
	return p0.first * p1.first + p0.second * p1.second;
}

// Function to calculate the max from a vector of floats
float max(vector<float> t)
{
	float maximum = INT_MIN;
	for (int i = 0; i < t.size(); i++)
		if (t[i] > maximum)
			maximum = t[i];
	return maximum;
}

// Function to calculate the min from a vector of floats
float min(vector<float> t)
{
	float minimum = INT_MAX;
	for (int i = 0; i < t.size(); i++)
		if (t[i] < minimum)
			minimum = t[i];
	return minimum;
}

// Cyrus Beck function, returns a pair of values
// that are then displayed as a line
pair<int, int>* CyrusBeck(pair<int, int> vertices[],
						pair<int, int> line[], int n)
{

	// Temporary holder value that will be returned
	pair<int, int>* newPair = new pair<int, int>[2];

	// Normals initialized dynamically(can do it statically also, doesn't matter)
	pair<int, int>* normal = new pair<int, int>[n];

	// Calculating the normals
	for (int i = 0; i < n; i++) {
		normal[i].second = vertices[(i + 1) % n].first - vertices[i].first;
		normal[i].first = vertices[i].second - vertices[(i + 1) % n].second;
	}

	// Calculating P1 - P0
	pair<int, int> P1_P0
		= make_pair(line[1].first - line[0].first,
					line[1].second - line[0].second);

	// Initializing all values of P0 - PEi
	pair<int, int>* P0_PEi = new pair<int, int>[n];

	// Calculating the values of P0 - PEi for all edges
	for (int i = 0; i < n; i++) {

		// Calculating PEi - P0, so that the
		// denominator won't have to multiply by -1
		P0_PEi[i].first
			= vertices[i].first - line[0].first;

		// while calculating 't'
		P0_PEi[i].second = vertices[i].second - line[0].second;
	}

	int *numerator = new int[n], *denominator = new int[n];

	// Calculating the numerator and denominators
	// using the dot function
	for (int i = 0; i < n; i++) {
		numerator[i] = dot(normal[i], P0_PEi[i]);
		denominator[i] = dot(normal[i], P1_P0);
	}

	// Initializing the 't' values dynamically
	float* t = new float[n];

	// Making two vectors called 't entering'
	// and 't leaving' to group the 't's
	// according to their denominators
	vector<float> tE, tL;

	// Calculating 't' and grouping them accordingly
	for (int i = 0; i < n; i++) {

		t[i] = (float)(numerator[i]) / (float)(denominator[i]);

		if (denominator[i] > 0)
			tE.push_back(t[i]);
		else
			tL.push_back(t[i]);
	}

	// Initializing the final two values of 't'
	float temp[2];

	// Taking the max of all 'tE' and 0, so pushing 0
	tE.push_back(0.f);
	temp[0] = max(tE);

	// Taking the min of all 'tL' and 1, so pushing 1
	tL.push_back(1.f);
	temp[1] = min(tL);

	// Entering 't' value cannot be
	// greater than exiting 't' value,
	// hence, this is the case when the line
	// is completely outside
	if (temp[0] > temp[1]) {
		newPair[0] = make_pair(-1, -1);
		newPair[1] = make_pair(-1, -1);
		return newPair;
	}

	// Calculating the coordinates in terms of x and y
	newPair[0].firs
		t
		= (float)line[0].first
		+ (float)P1_P0.first * (float)temp[0];
	newPair[0].second
		= (float)line[0].second
		+ (float)P1_P0.second * (float)temp[0];
	newPair[1].first
		= (float)line[0].first
		+ (float)P1_P0.first * (float)temp[1];
	newPair[1].second
		= (float)line[0].second
		+ (float)P1_P0.second * (float)temp[1];
	cout << '(' << newPair[0].first << ", "
		<< newPair[0].second << ") ("
		<< newPair[1].first << ", "
		<< newPair[1].second << ")";

	return newPair;
}

// Driver code
int main()
{

	// Setting up a window and loop
	// and the vertices of the polygon and line
	RenderWindow window(VideoMode(500, 500), "Cyrus Beck");
	pair<int, int> vertices[]
		= { make_pair(200, 50),
			make_pair(250, 100),
			make_pair(200, 150),
			make_pair(100, 150),
			make_pair(50, 100),
			make_pair(100, 50) };

	// Make sure that the vertices
	// are put in a clockwise order
	int n = sizeof(vertices) / sizeof(vertices[0]);
	pair<int, int> line[] = { make_pair(10, 10), make_pair(450, 200) };
	pair<int, int>* temp1 = CyrusBeck(vertices, line, n);
	pair<int, int> temp2[2];
	temp2[0] = line[0];
	temp2[1] = line[1];

	// To allow clipping and unclipping
	// of the line by just pressing a key
	bool trigger = false;
	while (window.isOpen()) {
		window.clear();
		Event event;
		if (window.pollEvent(event)) {
			if (event.type == Event::Closed)
				window.close();
			if (event.type == Event::KeyPressed)
				trigger = !trigger;
		}
		drawPolygon(&window, vertices, n);

		// Using the trigger value to clip
		// and unclip a line
		if (trigger) {
			line[0] = temp1[0];
			line[1] = temp1[1];
		}
		else {
			line[0] = temp2[0];
			line[1] = temp2[1];
		}
		drawline(&window, line[0], line[1]);
		window.display();
	}
	return 0;
}
