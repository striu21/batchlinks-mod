import fall
import platform

if platform.system() == "Windows":
    if not fall.is_installed("gdown"):
        fall.run_pip("install gdown", "requirements for Batchlinks Download extension")

    if not fall.is_installed("wget"):
        fall.run_pip("install wget", "requirements for Batchlinks Download extension")
