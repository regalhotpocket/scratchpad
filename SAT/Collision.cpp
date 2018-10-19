#include "Collision.h"

void col::Collision::move(double x_shift, double y_shift)
{
	for (size_t i = 0; i < points.size(); i++)
	{
		points[i].x += x_shift;
		points[i].y += y_shift;
	}
}
const std::vector<col::cvector>& col::Collision::get_points()
{
	return points;
}
void col::Collision::set_point(int index, int x, int y)
{
	points[index] = { (double)x, (double)y };
}
void col::Collision::push_point(int x, int y)
{
	points.push_back({ (double)x, (double)y });
}

col::cvector col::prep(std::vector<cvector> &points, int i)
{
	cvector p1 = points[i];
	cvector p2 = points[i + 1 == points.size() ? 0 : i + 1];
	cvector axsis;
	axsis.x = -(p2.y - p1.y);
	axsis.y = p2.x - p1.x;
	double len = sqrt(pow(axsis.x, 2) + pow(axsis.y, 2));
	axsis.x = axsis.x / len;
	axsis.y = axsis.y / len;
	if (axsis.x*axsis.y < 0)
	{
		axsis.x = -abs(axsis.x);
		axsis.y = abs(axsis.y);
	}
	else
	{
		axsis.x = abs(axsis.x);
		axsis.y = abs(axsis.y);
	}
	return axsis;
}
col::range col::project(const std::vector<cvector> points, const cvector axis)
{
	float min = (points[0].x*axis.x + points[0].y*axis.y);
	float max = min;
	for (int i = 0; i < points.size(); i++)
	{
		float proj = (points[i].x*axis.x + points[i].y*axis.y);
		if (proj < min) min = proj;
		if (proj > max) max = proj;
	}
	return{ min, max };
}
double col::overlap(range lhs, range rhs)
{
	return ((lhs.max > rhs.max) ? rhs.max : lhs.max) - ((lhs.min > rhs.min) ? lhs.min : rhs.min);
}
col::result col::intersecting(Collision & rhs, Collision & lhs)
{
	double min_projection = 100000;
	cvector angle_of_min;

	for (size_t i = 0; i < rhs.points.size(); i++)
	{
		cvector axsis = prep(rhs.points, i);
		range proj_lhs = project(rhs.points, axsis), proj_rhs = project(lhs.points, axsis);
		double overlap_results = overlap(proj_lhs, proj_rhs);
		if (overlap_results <= 0) return{ false,{ 0,0 },0 };
		else if (overlap_results < min_projection)
		{
			min_projection = overlap_results;
			angle_of_min = axsis;
		}
	}
	for (size_t i = 0; i < lhs.points.size(); i++)
	{
		cvector axsis = prep(lhs.points, i);
		range proj_lhs = project(rhs.points, axsis), proj_rhs = project(lhs.points, axsis);
		double overlap_results = overlap(proj_lhs, proj_rhs);
		if (overlap_results <= 0) return{ false,{ 0,0 },0 };
		else if (overlap_results < min_projection)
		{
			min_projection = overlap_results;
			angle_of_min = axsis;
		}
	}
	return{ true, angle_of_min, min_projection };
}