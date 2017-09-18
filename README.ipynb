{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Question 1\n",
    "\n",
    "If you break a stick in two places at random, forming three pieces, what is the probability of being able to form a triangle with the pieces?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### Triangle inequality princple\n",
    "c – b < a < c + b \n",
    "\n",
    "or \n",
    "\n",
    "a + b > c  \n",
    "b + c > a  \n",
    "a + c > b\n",
    "\n",
    "The underlying basis of how I preceded is the triangle inequality principle. I haven't taken geometry since high school, so relied on sparknotes and teacher websites. My understanding is that triangles can only be made by lines that meet the above criteria. I saw two different forms of it, and I decided to use the first rule. If this is incorrect, then everything moving forward is irrelevant to the questions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import random as rad\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "#The input is the stick length, and the randomness is the two breaks\n",
    "def stick_triangle (trials, stick):\n",
    "    true_list = 0\n",
    "    false_list = 0\n",
    "    #Trials are to obtain a simulation. The result is a binary result of True, a triangle is achieved, and False, \n",
    "    #a triangle is impossible. The results are accrued over the trials. \n",
    "    for _ in range (trials):\n",
    "        #So piece a is the break of the stick at a random percent of the stick\n",
    "        first_break = rad.random()\n",
    "        a = first_break*stick\n",
    "        #The remaining stick is the stick minus the broken a piece, or b+c\n",
    "        remaining_stick = stick - a\n",
    "        #Calculate b similar to a\n",
    "        second_break  = rad.random()\n",
    "        b = second_break*remaining_stick\n",
    "        #Part \n",
    "        c = remaining_stick - b\n",
    "        # Now I aggregate the results. \n",
    "        if ((c+b) > a > (c-b)) == True:\n",
    "            true_list = true_list +1\n",
    "        else: \n",
    "            false_list = false_list+1\n",
    "            \n",
    "    triangle_prob = true_list/trials\n",
    "    return true_list, false_list, triangle_prob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3465168, 6534832, 0.3465168)"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trials = 10000000\n",
    "stick = rad.randrange(999)\n",
    "stick_triangle (trials, stick)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Question 2\n",
    "\n",
    "If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form a triangle with them?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#For the second question, I approached it in the same fashion as the first. \n",
    "#I just obtained three random numbers between 0 to 1. \n",
    "def rand_sticks_triangle (trials):\n",
    "    true = 0\n",
    "    false = 0\n",
    "    \n",
    "    for _ in range (trials):\n",
    "        a = rad.random()\n",
    "        b = rad.random ()\n",
    "        c = rad.random()\n",
    "        if ((c+b) > a > (c-b)) == True:\n",
    "            true = true +1\n",
    "        else: \n",
    "            false = false+1\n",
    "    triangle_prob = true/trials\n",
    "    return true, false, triangle_prob\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6666829, 3333171, 0.6666829)"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trials = 10000000\n",
    "rand_sticks_triangle (trials)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Question 3\n",
    "\n",
    "If you break a stick in two places at random, what is the probability of being able to form an acute triangle — where each angle is less than 90 degrees — with the pieces?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#The third question, works the same as the first, just with the addition of a boolean to determine if the triangle is acute. \n",
    "def acute_stick (trials, stick):\n",
    "    true = 0\n",
    "    false = 0\n",
    "    for _ in range (trials):\n",
    "        \n",
    "        first_break = rad.random()\n",
    "        a = first_break*stick\n",
    "        \n",
    "        remaining_stick = stick - a\n",
    "        \n",
    "        second_break  = rad.random()\n",
    "        b = second_break*remaining_stick\n",
    "        \n",
    "        c = remaining_stick - b\n",
    "        \n",
    "        a_sq = a*a\n",
    "        b_sq = b*b\n",
    "        c_sq = c*c\n",
    "        \n",
    "        if ((c+b) > a > (c-b)) and ((a_sq+b_sq)>c_sq):\n",
    "            true = true+1\n",
    "        else:\n",
    "            false = false +1\n",
    "    acute_triangle_prob = true/trials \n",
    "    return true, false, acute_triangle_prob \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3068576, 6931424, 0.3068576)"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trials = 10000000\n",
    "stick = rad.randrange(999)\n",
    "\n",
    "acute_stick( trials, stick)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Question 4\n",
    "\n",
    "If you select three sticks, each of random length (between 0 and 1), what is the probability of being able to form an acute triangle with the sticks?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Originally, I attempted to do this similar to Question 2 and 3, but I realized for the pythagorean theorem \n",
    "#C is the hypoteneuse and A and B are the other sides. Therefore when determining c, a, and b, c must be the \n",
    "#max of the three. Therefore, I devised a series of max, and sides (less_) to then determine the order in the boolean.\n",
    "\n",
    "def rand_sticks_right (trials):\n",
    "    true = 0\n",
    "    false = 0\n",
    "    \n",
    "    for _ in range (trials):\n",
    "        a = rad.random()\n",
    "        b = rad.random ()\n",
    "        c = rad.random()\n",
    "        a_sq = a*a\n",
    "        b_sq = b*b\n",
    "        c_sq = c*c\n",
    "        max = 3\n",
    "        less_1 = 1\n",
    "        less_2 = 2\n",
    "        if (c>(a and b)):\n",
    "            max = c_sq\n",
    "            less_1 = a_sq\n",
    "            less_2 = b_sq\n",
    "        \n",
    "        if (b>(c and a)):\n",
    "            max = b_sq\n",
    "            less_1 =a_sq\n",
    "            less_2 = c_sq\n",
    "        if (a>(b and c)):\n",
    "            max = a_sq\n",
    "            less_1 =b_sq\n",
    "            less_2 = c_sq\n",
    "        if (max==(less_1+less_2)):\n",
    "            true = true+1\n",
    "        else: \n",
    "            false = false+1\n",
    "    \n",
    "    right_tri_prob = true/trials\n",
    "    return true, false, right_tri_prob, trials\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0, 100000000, 0.0, 100000000)"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "trials = 100000000 \n",
    "rand_sticks_right (trials)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
