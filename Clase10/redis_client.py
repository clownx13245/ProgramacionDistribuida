import redis
# Conexion a Redis (Coordinador)
r = redis.Redis(host='localhost', port=6379,decode_responses=True)