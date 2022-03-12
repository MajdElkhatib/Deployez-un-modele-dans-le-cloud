
# Importer des bibliothèques

import sys, os
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, element_at
from sparkdl import DeepImageFeaturizer
from datetime import datetime


# 1-Créer une SparkSession

spark = (
    SparkSession
    .builder
    .appName("projet8_featurizer_img")
    .getOrCreate()
)


# 2-Chargement des images

ROOT_PATH = sys.argv[1]

# les images de jeu de données Training (original size)
DATA_PATH = os.path.join(ROOT_PATH, "Data1/Training/**")

print("Chargement des images...")
image_df = (
    spark
    .read
    .format("image")
    .load(DATA_PATH)
)

# 3-Échantillon pour tester
image_df = image_df.limit(400)

# le partitionnement est un moyen de diviser les données en plusieurs partitions afin que vous puissiez exécuter des transformations sur
# plusieurs partitions en parallèle, ce qui permet de terminer le travail plus rapidement
image_df = image_df.repartition(40) 

print("Nb de partitions:", image_df.rdd.getNumPartitions())


# 4-Obtenir les labels (targets) : son dernier répertoire 

image_df = (image_df
            .withColumn(
                'label',
                element_at(
                    split(
                        image_df['image.origin'],
                        "/"),
                    -2)))


# 5-Preprocessing et Réduction de dimension

from sparkdl import DeepImageFeaturizer

featurizer = DeepImageFeaturizer(
    inputCol="image",
    outputCol="features", 
    modelName="ResNet50"  # Instanciation featurizer généré par ResNet50                         
)                         # Renvoie un vecteur de feature de taille 2048


# PCA on the extracted features

from pyspark.ml.feature import PCA
pca = PCA(k=10,
          inputCol="features",
          outputCol="pca_features")

# Mettre feature extractor et PCA en pipeline

from pyspark.ml import Pipeline
pipe = Pipeline(stages=[featurizer, pca])
extractor = pipe.fit(image_df)
image_df = extractor.transform(image_df).select("features", "pca_features","label", "image.origin")


# 6-Enregistrer les résultats : Parquet file


now = datetime.now()
    
# Converting to string in the format dd-mm-YY H:M:S
t_string = now.strftime("%b-%d-%Y %H:%M:%S")

# Création du PATH pour stocker les résultats
RESULTS_PATH = os.path.join(ROOT_PATH, "results", t_string)

image_df.write.format("parquet").mode("overwrite").save(RESULTS_PATH)


# 7-Fermer sparkSession
spark.stop()
print("Spark application terminé avec succès.")