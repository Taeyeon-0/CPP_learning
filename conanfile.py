from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("spdlog/1.17.0")

    def layout(self):
        build_type = str(self.settings.build_type)
        self.folders.build = f"build/{build_type}"
        self.folders.generators = f"build/{build_type}/generators"
        self.folders.source = "src"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generator = "Ninja"
        tc.generate()
