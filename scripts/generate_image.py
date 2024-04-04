# %%
import enum


class Color(enum.Enum):
    RED   = 1
    GREEN = 2
    BLUE  = 3

class Shape(enum.Enum):
    CIRCLE   = 1
    TRIANGLE = 2
    SQUARE   = 3


n_shapes = 4

# %%
import argparse

parser = argparse.ArgumentParser(description="Creates image and csv for trials")
parser.add_argument("--chunk", help='Path to the "chunk_includes" directory')
args = parser.parse_args()

chunk_includes_dir = "./"
chunk_includes_dir = "../chunk_includes/"
if arg.chunk:
	chunk_includes_dir = arg.chunk

# %%
"""
Poorman's constraint programming
"""


class Trial:
	def __init__(self):
		self.generate()

	def find_solution(self):
		while not self.constraint():
			self.generate()
		return self

	def generate(self):
		pass

	def constraint(self):
		return True

class TargetTrial(Trial):
	def generate(self):
		self.sentence_shape = random.choice(list(Shape))
		self.sentence_color = random.choice(list(Color))

		self.shapes = [random.choice(list(Shape)) for _ in range(n_shapes)]
		self.colors = [random.choice(list(Color)) for _ in range(n_shapes)]

	def pretty_print(self):
		print(self.sentence())
		print(f"Color: {self.sentence_color.name}")
		print(f"Shape: {self.sentence_shape.name}")
		self.pic_pretty_print()

	def sentence(self):
		return f"There is a {self.sentence_shape.name.lower()} and it is {self.sentence_color.name.lower()}."

	def pic_pretty_print(self):
		for (i, (color, shape)) in enumerate(zip(self.colors, self.shapes)):
			print(f"{i}: {color.name} {shape.name}")

class TargetNegTrial(TargetTrial):
	def sentence(self):
		return f"There is a {self.sentence_shape.name.lower()} and it isn't {self.sentence_color.name.lower()}."




class ControlTrial(TargetTrial):
	def generate(self):
		super(ControlTrial, self).generate()
		self.sentence_other_shape = random.choice([shape for shape in Shape if shape != self.sentence_shape])

	def sentence(self):
		return f"There is a {self.sentence_shape.name.lower()} and the {self.sentence_other_shape.name.lower()} is {self.sentence_color.name.lower()}"


	def pretty_print(self):
		print(self.sentence())
		print(f"Color: {self.sentence_color.name}")
		print(f"Shape: {self.sentence_shape.name}")
		print(f"Other shape: {self.sentence_other_shape.name}")
		self.pic_pretty_print()


# %%
import random



# class TargetTrialPosUnique(TargetTrial):
# 	def constraint(model):
# 		"""
# 		Condition POS-UNIQUE
# 		  - exactly one SHAPE
# 		  - it is of COLOR
# 		"""
# 		only_one_shape = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 1
# 		shape_is_color = all(
# 			(shape != model.sentence_shape) or (color == model.sentence_color) 
# 			for (shape, color) in zip(model.shapes, model.colors)
# 		)
# 		return only_one_shape and shape_is_color

class TargetTrialPosForAll(TargetTrial):
	def constraint(model):
		"""
		Condition POS-FORALL
		  - two SHAPEs
		  - both are COLORs
		"""
		two_shapes = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 2
		shape_is_color = all(
			(shape != model.sentence_shape) or (color == model.sentence_color) 
			for (shape, color) in zip(model.shapes, model.colors)
		)
		return two_shapes and shape_is_color

class TargetTrialPosExists(TargetTrial):
	def constraint(model):
		"""
		Condition POS-EXISTS
		  - two SHAPEs
		  - one is COLOR
		  - the other is not
		"""
		two_shapes = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 2
		one_shape_is_color = sum(
			1
			for (shape, color) in zip(model.shapes, model.colors)
			if shape == model.sentence_shape and color == model.sentence_color
		) == 1
		return two_shapes and one_shape_is_color


class TargetTrialPosConj2False(TargetTrial):
	def constraint(model):
		"""
		Condition POS-CONJ2-FALSE
		  - one SHAPE
		  - it is not COLOR
		"""
		only_one_shape    = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 1
		shape_isnot_color = not any(
			shape == model.sentence_shape and color == model.sentence_color
			for (shape, color) in zip(model.shapes, model.colors)
		)
		return only_one_shape and shape_isnot_color

class TargetTrialPosConj1False(TargetTrial):
	def constraint(model):
		"""
		Condition POS-CONJ2-FALSE
		  - no SHAPE
		"""
		no_shape = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 0
		return no_shape



# class TargetTrialNegUnique(TargetNegTrial):
# 	def constraint(model):
# 		"""
# 		Condition NEG-UNIQUE
# 		  - one SHAPEs
# 		  - one is not COLOR
# 		"""
# 		# Only one shape
# 		only_one_shape = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 1
# 		shape_is_color = all(
# 			(shape != model.sentence_shape) or (color != model.sentence_color) 
# 			for (shape, color) in zip(model.shapes, model.colors)
# 		)
# 		return only_one_shape and shape_is_color

class TargetTrialNegForall(TargetNegTrial):
	def constraint(model):
		"""
		Condition NEG-FORALL
		  - two SHAPEs
		  - none is COLOR
		"""
		two_shapes = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 2
		shapes_are_color = all(
			(shape != model.sentence_shape) or (color != model.sentence_color) 
			for (shape, color) in zip(model.shapes, model.colors)
		)
		return two_shapes and shapes_are_color

class TargetTrialNegExists(TargetNegTrial):
	def constraint(model):
		"""
		Condition NEG-EXISTS
		  - two SHAPEs
		  - one is COLOR
		  - the other is not
		"""
		two_shapes = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 2
		one_shape_is_color = sum(
			1
			for (shape, color) in zip(model.shapes, model.colors)
			if shape == model.sentence_shape and color == model.sentence_color
		) == 1
		return two_shapes and one_shape_is_color


class TargetTrialNegConj2False(TargetNegTrial):
	def constraint(model):
		"""
		Condition NEG-CONJ2-FALSE
		  - one SHAPE
		  - it is COLOR
		"""
		only_one_shape    = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 1
		shape_isnot_color = not any(
			shape == model.sentence_shape and color != model.sentence_color
			for (shape, color) in zip(model.shapes, model.colors)
		)
		return only_one_shape and shape_isnot_color

class TargetTrialNegConj1False(TargetNegTrial):
	def constraint(model):
		"""
		Condition NEG-CONJ1-FALSE
		  - no shape
		"""
		no_shape = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 0
		return no_shape



class ControlTrialConj1False(ControlTrial):
	def constraint(model):
		"""
		Condition CONTROL-CONJ1-FALSE
		  - no SHAPE
		  - one OTHER_SHAPE 
		  - other shape is COLOR
		"""
		no_shape = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 0
		one_other_shape = sum(1 for shape in model.shapes if shape == model.sentence_other_shape) == 1
		other_shape_is_color = all(
			color == model.sentence_color
			for (shape, color) in zip(model.shapes, model.colors)
			if shape == model.sentence_other_shape
		)
		return no_shape and one_other_shape and other_shape_is_color


class ControlTrialConj2False(ControlTrial):
	def constraint(model):
		"""
		Condition CONTROL-CONJ1-FALSE
		  - one SHAPE
		  - one OTHER_SHAPE 
		  - other shape is not COLOR
		"""
		no_shape = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 1
		one_other_shape = sum(1 for shape in model.shapes if shape == model.sentence_other_shape) == 1
		other_shape_is_not_color = all(
			color != model.sentence_color
			for (shape, color) in zip(model.shapes, model.colors)
			if shape == model.sentence_other_shape
		)
		return no_shape and one_other_shape and other_shape_is_not_color

class ControlTrialTrue(ControlTrial):
	def constraint(model):
		"""
		Condition CONTROL-CONJ1-FALSE
		  - one SHAPE
		  - one OTHER_SHAPE 
		  - other shape is COLOR
		"""
		no_shape = sum(1 for shape in model.shapes if shape == model.sentence_shape) == 1
		one_other_shape = sum(1 for shape in model.shapes if shape == model.sentence_other_shape) == 1
		other_shape_is_not_color = all(
			color == model.sentence_color
			for (shape, color) in zip(model.shapes, model.colors)
			if shape == model.sentence_other_shape
		)
		return no_shape and one_other_shape and other_shape_is_not_color



trials = [
	# TargetTrialPosUnique, 
	# TargetTrialPosForAll, 
	# TargetTrialPosExists, 
	# TargetTrialPosConj2False, 
	# TargetTrialPosConj1False,

	# TargetTrialNegUnique, 
	# TargetTrialNegForall, 
	# TargetTrialNegExists, 
	# TargetTrialNegConj2False, 
	# TargetTrialNegConj1False,

	# ControlTrialConj1False,
	# ControlTrialConj2False,
	ControlTrialTrue,
]

random.seed(23012202)

for GivenTrial in trials:
	print("========================")
	print(GivenTrial.__name__)
	print()
	for _ in range(10):
		model = GivenTrial().find_solution()
		model.pretty_print()
		# import pdb; pdb.set_trace()
		print()



# %%
import cairo

color_mapping = {
    Color.RED: (1., 0., 0.),
    Color.GREEN: (0., 1., 0.),
    Color.BLUE: (0., 0., 1.)
}

def draw_circle(context, color):
    context.set_source_rgb(*color_mapping[color])
    context.arc(0, 0.1 * 50, 0.9 * 50, 0, 2 * 3.14159)
    context.fill()

def draw_triangle(context, color):
    context.set_source_rgb(*color_mapping[color])
    SIDE_TRIANGLE = 100
    context.move_to(0, SIDE_TRIANGLE * (1 /2 -  3 ** 0.5 / 2))
    context.line_to(- SIDE_TRIANGLE / 2, SIDE_TRIANGLE / 2)
    context.line_to(  SIDE_TRIANGLE / 2, SIDE_TRIANGLE / 2)
    context.close_path()
    context.fill()

def draw_square(context, color):
    context.set_source_rgb(*color_mapping[color])
    context.rectangle(-50, -50, 100, 100)
    context.fill()

# Example usage:

shape_mapping = {
	Shape.CIRCLE   : draw_circle,
	Shape.SQUARE   : draw_square,
	Shape.TRIANGLE : draw_triangle,
}

def draw_model(model, filepath):
	SQUARE_SIZE = 120


	surface = cairo.SVGSurface(filepath, 2 * SQUARE_SIZE, 2 * SQUARE_SIZE)
	context = cairo.Context(surface)

	centers = [
		(SQUARE_SIZE / 2,     SQUARE_SIZE / 2),
		(SQUARE_SIZE / 2,     SQUARE_SIZE * 3 / 2),
		(SQUARE_SIZE * 3 / 2, SQUARE_SIZE / 2),
		(SQUARE_SIZE * 3 / 2, SQUARE_SIZE * 3 / 2),
	]

	for (color, shape, center) in zip(model.colors, model.shapes, centers):
		context.save()
		context.translate(*center)  # Centering the shapes
		shape_mapping[shape](context, color)
		context.restore()


	surface.finish()


# %%
import csv
import os

trials = [
	(3, "pos",     "forall",        TargetTrialPosForAll), 
	(3, "pos",     "exists",        TargetTrialPosExists), 
	(3, "pos",     "conj2false",    TargetTrialPosConj2False), 
	(3, "pos",     "conj1false",    TargetTrialPosConj1False),

	(3, "neg",     "forall",        TargetTrialNegForall), 
	(3, "neg",     "exists",        TargetTrialNegExists), 
	(3, "neg",     "conj1false",    TargetTrialNegConj1False),
	(3, "neg",     "conj2false",    TargetTrialNegConj2False), 

	(3, "control", "conj1false",    ControlTrialConj1False),
	(3, "control", "conj2false",    ControlTrialConj2False),
	(6, "control", "true",          ControlTrialTrue),
]


with open(os.path.join(chunk_includes_dir, "trials.csv"), "w") as file:
	writer = csv.DictWriter(file, fieldnames=[
		"trial_no",

		"sentence",
		"group",
		"condition",
		"full_condition",

		"shape0", "shape1", "shape2", "shape3",
		"color0", "color1", "color2", "color3",

		"filename",
	])
	writer.writeheader()

	for n_trials, group, condition, GivenTrial in trials:
		

		for i in range(n_trials):
			model = GivenTrial().find_solution()


			full_condition = f"{group}_{condition}"
			filename = f"{full_condition}_{i}.svg"

			draw_model(model, os.path.join(chunk_includes_dir, filename))

			writer.writerow({
				"trial_no" : i,
				"sentence" : model.sentence(),


				"group" :          group,
				"condition" :      condition,
				"full_condition" : full_condition,

				"shape0" : model.shapes[0].name, "shape1" : model.shapes[1].name, "shape2" : model.shapes[2].name, "shape3" : model.shapes[3].name,
				"color0" : model.colors[0].name, "color1" : model.colors[1].name, "color2" : model.colors[2].name, "color3" : model.colors[3].name,

				"filename" : filename,
			})


