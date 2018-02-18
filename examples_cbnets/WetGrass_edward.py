import numpy as np
import tensorflow as tf
import edward as ed
import edward.models as edm


# node names in lexicographic (alphabetic) order
nd_names_lex_ord = ['Cloudy', 'Rain', 'Sprinkler', 'WetGrass']

# node names in topological (chronological) order
nd_names_topo_ord = ['Cloudy', 'Rain', 'Sprinkler', 'WetGrass']

with tf.name_scope('model'):
    Cloudy = tf.placeholder(tf.float32, [None, 2],
        name="Cloudy")

    arr_Rain = np.array([[ 0.4,  0.6],
       [ 0.5,  0.5]])
    p_Rain = tf.convert_to_tensor(arr_Rain, dtype=tf.float32)[
        Cloudy, :]
    Rain = edm.Categorical(
        probs=p_Rain, name='Rain')

    arr_Sprinkler = np.array([[ 0.2,  0.8],
       [ 0.7,  0.3]])
    p_Sprinkler = tf.convert_to_tensor(arr_Sprinkler, dtype=tf.float32)[
        Cloudy, :]
    Sprinkler = edm.Categorical(
        probs=p_Sprinkler, name='Sprinkler')

    arr_WetGrass = np.array([[[ 0.99,  0.01],
        [ 0.01,  0.99]],

       [[ 0.01,  0.99],
        [ 0.01,  0.99]]])
    p_WetGrass = tf.convert_to_tensor(arr_WetGrass, dtype=tf.float32)[
        Sprinkler, Rain, :]
    WetGrass = edm.Categorical(
        probs=p_WetGrass, name='WetGrass')

with tf.name_scope('posterior'):
    Cloudy_q = edm.Categorical(
        probs=tf.nn.softmax(tf.get_variable('Cloudy_q/probs', shape=[2])),
        name='Cloudy_q')

    Rain_q = edm.Categorical(
        probs=tf.nn.softmax(tf.get_variable('Rain_q/probs', shape=[2])),
        name='Rain_q')

    Sprinkler_q = edm.Categorical(
        probs=tf.nn.softmax(tf.get_variable('Sprinkler_q/probs', shape=[2])),
        name='Sprinkler_q')

    WetGrass_q = edm.Categorical(
        probs=tf.nn.softmax(tf.get_variable('WetGrass_q/probs', shape=[2])),
        name='WetGrass_q')
