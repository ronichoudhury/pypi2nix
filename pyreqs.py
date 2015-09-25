import pip
import semantic_version
import sys


def main():
    if len(sys.argv) < 2:
        print >>sys.stderr, "usage: pyreqs.py <package>"
        return 1

    package = sys.argv[1]

    dists = pip.get_installed_distributions()
    found = filter(lambda x: x.key == package, dists)

    if not found:
        print >>sys.stderr, "package %s not installed" % (package)
        return 1

    if len(found) > 1:
        print >>sys.stderr, "bizarre error; package %s installed more than once" % (package)
        return 1

    found = found[0]
    requires = found.requires()

    keys = map(lambda x: x.key, requires);
    specs = map(lambda x: semantic_version.Spec(str(x.specifier)), requires)

    print zip(keys, specs)


if __name__ == "__main__":
    sys.exit(main())
