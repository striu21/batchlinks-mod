import sus
import platform

if platform.system() == "Windows":
    if not sus.is_installed("gdown"):
        sus.run_pip("install gdown", "requirements for Batchlinks Download extension")

    if not sus.is_installed("wget"):
        sus.run_pip("install wget", "requirements for Batchlinks Download extension")
