#pragma once
#include <vector>

namespace col
{
	struct cvector {
		double x, y;
	};
	struct range {
		double min, max;
	};
	struct result {
		bool truth;
		cvector projection;
		double min_projection;
	};

	class Collision
	{
		friend result intersecting(Collision &rhs, Collision &lhs);
	public:
		void move(double x_shift, double y_shift);
		const std::vector<cvector>& get_points();
		void set_point(int index, int x, int y);
		void push_point(int x, int y);
		virtual void reaction();
	private:
		std::vector<cvector> points;
	};
	result intersecting(Collision & lhs, Collision & rhs);
	range project(const std::vector<cvector> points, const cvector axis);
	double  overlap(range lhs, range rhs);
	cvector prep(std::vector<cvector> &points, int i);
}