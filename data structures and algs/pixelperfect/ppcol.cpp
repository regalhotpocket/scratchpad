bool bb_col(bb& bb_lhs, bb& bb_rhs) {
	if (bb_lhs.x < bb_rhs.x + bb_rhs.w &&
		bb_lhs.x + bb_lhs.w > bb_rhs.x &&
		bb_lhs.y < bb_rhs.y + bb_rhs.h &&
		bb_lhs.h + bb_lhs.y > bb_rhs.y)
		return true;
	else return false;
}

bool colliding(Object &lhs, Object &rhs) {
	if (bb_col(lhs.pos, rhs.pos)) {
		float colBot, colTop, colLeft, colRight;
		colTop   = max(lhs.pos.y, rhs.pos.y);
		colBot   = min(lhs.pos.y + lhs.pos.h, rhs.pos.y + rhs.pos.h);
		colLeft  = max(lhs.pos.x, rhs.pos.x);
		colRight = min(lhs.pos.x + lhs.pos.w, rhs.pos.x + rhs.pos.w);

		for (int i = (int)colTop; i < colBot; i++) {
			for (int j = (int)colLeft; j < colRight; j++) {
				if (    sf::Color::Black == lhs.image.getPixel((int)(j - lhs.pos.x), (int)(i - lhs.pos.y)) &&
					sf::Color::Black == rhs.image.getPixel((int)(j - rhs.pos.x), (int)(i - rhs.pos.y))
				   ) return true;
			}
		}
		return false;
	}
	else return false;
}