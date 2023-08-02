import pygame
def get_collision_side(rect_a, rect_b):
    # Get the center points of both rectangles
    center_a = rect_a.center
    center_b = rect_b.center

    # Calculate the differences in position between the centers of the rectangles
    dx = center_a[0] - center_b[0]
    dy = center_a[1] - center_b[1]

    # Calculate the combined half-width and half-height of the rectangles
    combined_half_width = (rect_a.width + rect_b.width) / 2
    combined_half_height = (rect_a.height + rect_b.height) / 2

    # Calculate the absolute differences in position
    abs_dx = abs(dx)
    abs_dy = abs(dy)

    # Calculate the overlap on both axes
    overlap_x = combined_half_width - abs_dx
    overlap_y = combined_half_height - abs_dy

    # Determine the collision side based on the overlap
    if overlap_x < overlap_y:
        if dx < 0:
            return "right"  # Collided on the right side of rect_b
        else:
            return "left"  # Collided on the left side of rect_b
    else:
        if dy < 0:
            return "bottom"  # Collided on the bottom side of rect_b
        else:
            return "top"  # Collided on the top side of rect_b

    # No collision detected
    return None